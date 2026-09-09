from __future__ import annotations

import json
import math
import re
from typing import Any, Optional, TypedDict, Union

_S: float = 1000
_M: float = _S * 60
_H: float = _M * 60
_D: float = _H * 24
_W: float = _D * 7
_Y: float = _D * 365.25
_MO: float = _Y / 12

StringValue = str


class Options(TypedDict, total=False):
    long: bool


_PARSE_RE = re.compile(
    r"^(?P<value>-?\d*\.?\d+) *"
    r"(?P<unit>milliseconds?|msecs?|ms|seconds?|secs?|s|minutes?|mins?|m|"
    r"hours?|hrs?|h|days?|d|weeks?|w|months?|mo|years?|yrs?|y)?$",
    re.IGNORECASE,
)


def _js_round(x: float) -> int:
    return math.floor(x + 0.5)


def _is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _is_string(x: Any) -> bool:
    return isinstance(x, str)


def _json_stringify(x: Any) -> str:
    try:
        return json.dumps(x)
    except (TypeError, ValueError):  # pragma: no cover
        return repr(x)


def parse(str_value: str) -> float:
    if not _is_string(str_value) or len(str_value) == 0 or len(str_value) > 100:
        raise ValueError(
            "Value provided to ms.parse() must be a string with length "
            f"between 1 and 99. value={_json_stringify(str_value)}"
        )
    match = _PARSE_RE.match(str_value)
    if match is None:
        return float("nan")
    value_str = match.group("value")
    unit_group = match.group("unit")
    unit = unit_group if unit_group is not None else "ms"
    n = float(value_str)
    u = unit.lower()
    if u in ("years", "year", "yrs", "yr", "y"):
        return n * _Y
    if u in ("months", "month", "mo"):
        return n * _MO
    if u in ("weeks", "week", "w"):
        return n * _W
    if u in ("days", "day", "d"):
        return n * _D
    if u in ("hours", "hour", "hrs", "hr", "h"):
        return n * _H
    if u in ("minutes", "minute", "mins", "min", "m"):
        return n * _M
    if u in ("seconds", "second", "secs", "sec", "s"):
        return n * _S
    if u in ("milliseconds", "millisecond", "msecs", "msec", "ms"):
        return n
    raise ValueError(  # pragma: no cover
        f'Unknown unit "{unit}" provided to ms.parse(). value={_json_stringify(str_value)}'
    )


def parse_strict(value: str) -> float:
    return parse(value)


def _fmt_short(ms_value: Union[int, float]) -> str:
    ms_abs = abs(ms_value)
    if ms_abs >= _Y:
        return f"{_js_round(ms_value / _Y)}y"
    if ms_abs >= _MO:
        return f"{_js_round(ms_value / _MO)}mo"
    if ms_abs >= _W:
        return f"{_js_round(ms_value / _W)}w"
    if ms_abs >= _D:
        return f"{_js_round(ms_value / _D)}d"
    if ms_abs >= _H:
        return f"{_js_round(ms_value / _H)}h"
    if ms_abs >= _M:
        return f"{_js_round(ms_value / _M)}m"
    if ms_abs >= _S:
        return f"{_js_round(ms_value / _S)}s"
    return f"{ms_value}ms"


def _plural(
    ms_value: Union[int, float],
    ms_abs: Union[int, float],
    n: Union[int, float],
    name: str,
) -> str:
    is_plural = ms_abs >= n * 1.5
    suffix = "s" if is_plural else ""
    return f"{_js_round(ms_value / n)} {name}{suffix}"


def _fmt_long(ms_value: Union[int, float]) -> str:
    ms_abs = abs(ms_value)
    if ms_abs >= _Y:
        return _plural(ms_value, ms_abs, _Y, "year")
    if ms_abs >= _MO:
        return _plural(ms_value, ms_abs, _MO, "month")
    if ms_abs >= _W:
        return _plural(ms_value, ms_abs, _W, "week")
    if ms_abs >= _D:
        return _plural(ms_value, ms_abs, _D, "day")
    if ms_abs >= _H:
        return _plural(ms_value, ms_abs, _H, "hour")
    if ms_abs >= _M:
        return _plural(ms_value, ms_abs, _M, "minute")
    if ms_abs >= _S:
        return _plural(ms_value, ms_abs, _S, "second")
    return f"{ms_value} ms"


def format(ms_value: Union[int, float], options: Optional[Options] = None) -> str:
    if not _is_number(ms_value) or not math.isfinite(ms_value):
        raise TypeError("Value provided to ms.format() must be of type number.")
    if options is not None and options.get("long"):
        return _fmt_long(ms_value)
    return _fmt_short(ms_value)


def ms(
    value: Union[str, int, float],
    options: Optional[Options] = None,
) -> Union[int, float, str]:
    if _is_string(value):
        return parse(value)
    if _is_number(value):
        return format(value, options)
    raise TypeError(
        f"Value provided to ms() must be a string or number. value={_json_stringify(value)}"
    )

# ms

Tiny millisecond conversion utility. Python port of [vercel/ms](https://github.com/vercel/ms).

Use this package to easily convert various time formats to milliseconds, and vice-versa.

## Examples

```python
from ms import ms

ms('2 days')   # 172800000
ms('1d')       # 86400000
ms('10h')      # 36000000
ms('2.5 hrs')  # 9000000
ms('2h')       # 7200000
ms('1m')       # 60000
ms('5s')       # 5000
ms('1y')       # 31557600000
ms('100')      # 100
ms('-3 days')  # -259200000
ms('-1h')      # -3600000
ms('-200')     # -200
```

### Convert from Milliseconds

```python
from ms import ms

ms(60000)             # "1m"
ms(2 * 60000)         # "2m"
ms(-3 * 60000)        # "-3m"
ms(ms('10 hours'))    # "10h"
```

### Long Format

```python
from ms import ms

ms(60000, {'long': True})           # "1 minute"
ms(2 * 60000, {'long': True})       # "2 minutes"
ms(-3 * 60000, {'long': True})      # "-3 minutes"
ms(ms('10 hours'), {'long': True})  # "10 hours"
```

### Individual Functions

`parse`, `parse_strict`, and `format` are also exported.

```python
from ms import parse, parse_strict, format

parse('1h')                        # 3600000
parse_strict('1h')                 # 3600000
format(3600000)                    # "1h"
format(3600000, {'long': True})    # "1 hour"
```

## Development

```
python3 -m pytest
```

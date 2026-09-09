import math

import pytest

from ms import ms


class TestMsString:
    def test_should_not_throw_an_error(self):
        ms("1m")

    def test_should_preserve_ms(self):
        assert ms("100") == 100

    def test_should_convert_from_m_to_ms(self):
        assert ms("1m") == 60000

    def test_should_convert_from_h_to_ms(self):
        assert ms("1h") == 3600000

    def test_should_convert_d_to_ms(self):
        assert ms("2d") == 172800000

    def test_should_convert_w_to_ms(self):
        assert ms("3w") == 1814400000

    def test_should_convert_s_to_ms(self):
        assert ms("1s") == 1000

    def test_should_convert_ms_to_ms(self):
        assert ms("100ms") == 100

    def test_should_convert_y_to_ms(self):
        assert ms("1y") == 31557600000

    def test_ms_string_should_work_with_decimals(self):
        assert ms("1.5h") == 5400000

    def test_should_work_with_multiple_spaces(self):
        assert ms("1   s") == 1000

    def test_should_return_nan_if_invalid(self):
        assert math.isnan(ms("\u2603"))
        assert math.isnan(ms("10-.5"))
        assert math.isnan(ms("ms"))

    def test_should_be_case_insensitive(self):
        assert ms("1.5H") == 5400000

    def test_should_work_with_numbers_starting_with_dot(self):
        assert ms(".5ms") == 0.5

    def test_should_work_with_negative_integers(self):
        assert ms("-100ms") == -100

    def test_should_work_with_negative_decimals(self):
        assert ms("-1.5h") == -5400000
        assert ms("-10.5h") == -37800000

    def test_should_work_with_negative_decimals_starting_with_dot(self):
        assert ms("-.5h") == -1800000


class TestMsLongString:
    def test_should_not_throw_an_error(self):
        ms("53 milliseconds")

    def test_should_convert_milliseconds_to_ms(self):
        assert ms("53 milliseconds") == 53

    def test_should_convert_msecs_to_ms(self):
        assert ms("17 msecs") == 17

    def test_should_convert_sec_to_ms(self):
        assert ms("1 sec") == 1000

    def test_should_convert_from_min_to_ms(self):
        assert ms("1 min") == 60000

    def test_should_convert_from_hr_to_ms(self):
        assert ms("1 hr") == 3600000

    def test_should_convert_days_to_ms(self):
        assert ms("2 days") == 172800000

    def test_should_convert_weeks_to_ms(self):
        assert ms("1 week") == 604800000

    def test_should_convert_years_to_ms(self):
        assert ms("1 year") == 31557600000

    def test_ms_long_string_should_work_with_decimals(self):
        assert ms("1.5 hours") == 5400000

    def test_should_work_with_negative_integers(self):
        assert ms("-100 milliseconds") == -100

    def test_should_work_with_negative_decimals(self):
        assert ms("-1.5 hours") == -5400000

    def test_should_work_with_negative_decimals_starting_with_dot(self):
        assert ms("-.5 hr") == -1800000


class TestMsNumberLong:
    def test_should_not_throw_an_error(self):
        ms(500, {"long": True})

    def test_should_support_milliseconds(self):
        assert ms(500, {"long": True}) == "500 ms"
        assert ms(-500, {"long": True}) == "-500 ms"

    def test_should_support_seconds(self):
        assert ms(1000, {"long": True}) == "1 second"
        assert ms(1200, {"long": True}) == "1 second"
        assert ms(10000, {"long": True}) == "10 seconds"

        assert ms(-1000, {"long": True}) == "-1 second"
        assert ms(-1200, {"long": True}) == "-1 second"
        assert ms(-10000, {"long": True}) == "-10 seconds"

    def test_should_support_minutes(self):
        assert ms(60 * 1000, {"long": True}) == "1 minute"
        assert ms(60 * 1200, {"long": True}) == "1 minute"
        assert ms(60 * 10000, {"long": True}) == "10 minutes"

        assert ms(-1 * 60 * 1000, {"long": True}) == "-1 minute"
        assert ms(-1 * 60 * 1200, {"long": True}) == "-1 minute"
        assert ms(-1 * 60 * 10000, {"long": True}) == "-10 minutes"

    def test_should_support_hours(self):
        assert ms(60 * 60 * 1000, {"long": True}) == "1 hour"
        assert ms(60 * 60 * 1200, {"long": True}) == "1 hour"
        assert ms(60 * 60 * 10000, {"long": True}) == "10 hours"

        assert ms(-1 * 60 * 60 * 1000, {"long": True}) == "-1 hour"
        assert ms(-1 * 60 * 60 * 1200, {"long": True}) == "-1 hour"
        assert ms(-1 * 60 * 60 * 10000, {"long": True}) == "-10 hours"

    def test_should_support_days(self):
        assert ms(1 * 24 * 60 * 60 * 1000, {"long": True}) == "1 day"
        assert ms(1 * 24 * 60 * 60 * 1200, {"long": True}) == "1 day"
        assert ms(6 * 24 * 60 * 60 * 1000, {"long": True}) == "6 days"

        assert ms(-1 * 1 * 24 * 60 * 60 * 1000, {"long": True}) == "-1 day"
        assert ms(-1 * 1 * 24 * 60 * 60 * 1200, {"long": True}) == "-1 day"
        assert ms(-1 * 6 * 24 * 60 * 60 * 1000, {"long": True}) == "-6 days"

    def test_should_support_weeks(self):
        assert ms(1 * 7 * 24 * 60 * 60 * 1000, {"long": True}) == "1 week"
        assert ms(2 * 7 * 24 * 60 * 60 * 1000, {"long": True}) == "2 weeks"

        assert ms(-1 * 1 * 7 * 24 * 60 * 60 * 1000, {"long": True}) == "-1 week"
        assert ms(-1 * 2 * 7 * 24 * 60 * 60 * 1000, {"long": True}) == "-2 weeks"

    def test_should_support_months(self):
        assert ms(30.4375 * 24 * 60 * 60 * 1000, {"long": True}) == "1 month"
        assert ms(30.4375 * 24 * 60 * 60 * 1200, {"long": True}) == "1 month"
        assert ms(30.4375 * 24 * 60 * 60 * 10000, {"long": True}) == "10 months"

        assert ms(-1 * 30.4375 * 24 * 60 * 60 * 1000, {"long": True}) == "-1 month"
        assert ms(-1 * 30.4375 * 24 * 60 * 60 * 1200, {"long": True}) == "-1 month"
        assert ms(-1 * 30.4375 * 24 * 60 * 60 * 10000, {"long": True}) == "-10 months"

    def test_should_support_years(self):
        assert ms(365.25 * 24 * 60 * 60 * 1000 + 1, {"long": True}) == "1 year"
        assert ms(365.25 * 24 * 60 * 60 * 1200 + 1, {"long": True}) == "1 year"
        assert ms(365.25 * 24 * 60 * 60 * 10000 + 1, {"long": True}) == "10 years"

        assert ms(-1 * 365.25 * 24 * 60 * 60 * 1000 - 1, {"long": True}) == "-1 year"
        assert ms(-1 * 365.25 * 24 * 60 * 60 * 1200 - 1, {"long": True}) == "-1 year"
        assert ms(-1 * 365.25 * 24 * 60 * 60 * 10000 - 1, {"long": True}) == "-10 years"

    def test_should_round(self):
        assert ms(234234234, {"long": True}) == "3 days"
        assert ms(-234234234, {"long": True}) == "-3 days"


class TestMsNumber:
    def test_should_not_throw_an_error(self):
        ms(500)

    def test_should_support_milliseconds(self):
        assert ms(500) == "500ms"
        assert ms(-500) == "-500ms"

    def test_should_support_seconds(self):
        assert ms(1000) == "1s"
        assert ms(10000) == "10s"

        assert ms(-1000) == "-1s"
        assert ms(-10000) == "-10s"

    def test_should_support_minutes(self):
        assert ms(60 * 1000) == "1m"
        assert ms(60 * 10000) == "10m"

        assert ms(-1 * 60 * 1000) == "-1m"
        assert ms(-1 * 60 * 10000) == "-10m"

    def test_should_support_hours(self):
        assert ms(60 * 60 * 1000) == "1h"
        assert ms(60 * 60 * 10000) == "10h"

        assert ms(-1 * 60 * 60 * 1000) == "-1h"
        assert ms(-1 * 60 * 60 * 10000) == "-10h"

    def test_should_support_days(self):
        assert ms(24 * 60 * 60 * 1000) == "1d"
        assert ms(24 * 60 * 60 * 6000) == "6d"

        assert ms(-1 * 24 * 60 * 60 * 1000) == "-1d"
        assert ms(-1 * 24 * 60 * 60 * 6000) == "-6d"

    def test_should_support_weeks(self):
        assert ms(1 * 7 * 24 * 60 * 60 * 1000) == "1w"
        assert ms(2 * 7 * 24 * 60 * 60 * 1000) == "2w"

        assert ms(-1 * 1 * 7 * 24 * 60 * 60 * 1000) == "-1w"
        assert ms(-1 * 2 * 7 * 24 * 60 * 60 * 1000) == "-2w"

    def test_should_support_months(self):
        assert ms(30.4375 * 24 * 60 * 60 * 1000) == "1mo"
        assert ms(30.4375 * 24 * 60 * 60 * 1200) == "1mo"
        assert ms(30.4375 * 24 * 60 * 60 * 10000) == "10mo"

        assert ms(-1 * 30.4375 * 24 * 60 * 60 * 1000) == "-1mo"
        assert ms(-1 * 30.4375 * 24 * 60 * 60 * 1200) == "-1mo"
        assert ms(-1 * 30.4375 * 24 * 60 * 60 * 10000) == "-10mo"

    def test_should_support_years(self):
        assert ms(365.25 * 24 * 60 * 60 * 1000 + 1) == "1y"
        assert ms(365.25 * 24 * 60 * 60 * 1200 + 1) == "1y"
        assert ms(365.25 * 24 * 60 * 60 * 10000 + 1) == "10y"

        assert ms(-1 * 365.25 * 24 * 60 * 60 * 1000 - 1) == "-1y"
        assert ms(-1 * 365.25 * 24 * 60 * 60 * 1200 - 1) == "-1y"
        assert ms(-1 * 365.25 * 24 * 60 * 60 * 10000 - 1) == "-10y"

    def test_should_round(self):
        assert ms(234234234) == "3d"
        assert ms(-234234234) == "-3d"


class TestMsInvalidInputs:
    def test_should_throw_an_error_when_ms_invalid_input_empty_string(self):
        with pytest.raises(Exception):
            ms("")

    def test_should_throw_an_error_when_ms_invalid_input_undefined(self):
        with pytest.raises(Exception):
            ms(None)

    def test_should_throw_an_error_when_ms_invalid_input_null(self):
        with pytest.raises(Exception):
            ms(None)

    def test_should_throw_an_error_when_ms_invalid_input_array(self):
        with pytest.raises(Exception):
            ms([])

    def test_should_throw_an_error_when_ms_invalid_input_object(self):
        with pytest.raises(Exception):
            ms({})

    def test_should_throw_an_error_when_ms_invalid_input_nan(self):
        with pytest.raises(Exception):
            ms(float("nan"))

    def test_should_throw_an_error_when_ms_invalid_input_infinity(self):
        with pytest.raises(Exception):
            ms(float("inf"))

    def test_should_throw_an_error_when_ms_invalid_input_negative_infinity(self):
        with pytest.raises(Exception):
            ms(float("-inf"))

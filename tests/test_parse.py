import math

import pytest

from ms import parse


class TestParseString:
    def test_should_not_throw_an_error(self):
        parse("1m")

    def test_should_preserve_ms(self):
        assert parse("100") == 100

    def test_should_convert_from_m_to_ms(self):
        assert parse("1m") == 60000

    def test_should_convert_from_h_to_ms(self):
        assert parse("1h") == 3600000

    def test_should_convert_d_to_ms(self):
        assert parse("2d") == 172800000

    def test_should_convert_w_to_ms(self):
        assert parse("3w") == 1814400000

    def test_should_convert_s_to_ms(self):
        assert parse("1s") == 1000

    def test_should_convert_ms_to_ms(self):
        assert parse("100ms") == 100

    def test_should_convert_y_to_ms(self):
        assert parse("1y") == 31557600000

    def test_parse_string_should_work_with_ms(self):
        assert parse("1.5h") == 5400000

    def test_should_work_with_multiple_spaces(self):
        assert parse("1   s") == 1000

    def test_should_return_nan_if_invalid(self):
        assert math.isnan(parse("\u2603"))
        assert math.isnan(parse("10-.5"))
        assert math.isnan(parse("foo"))

    def test_should_be_case_insensitive(self):
        assert parse("53 YeArS") == 1672552800000
        assert parse("53 WeEkS") == 32054400000
        assert parse("53 DaYS") == 4579200000
        assert parse("53 HoUrs") == 190800000
        assert parse("53 MiLliSeCondS") == 53

    def test_should_work_with_numbers_starting_with_dot(self):
        assert parse(".5ms") == 0.5

    def test_should_work_with_negative_integers(self):
        assert parse("-100ms") == -100

    def test_should_work_with_negative_decimals(self):
        assert parse("-1.5h") == -5400000
        assert parse("-10.5h") == -37800000

    def test_should_work_with_negative_decimals_starting_with_dot(self):
        assert parse("-.5h") == -1800000


class TestParseLongString:
    def test_should_not_throw_an_error(self):
        parse("53 milliseconds")

    def test_should_convert_milliseconds_to_ms(self):
        assert parse("53 milliseconds") == 53

    def test_should_convert_msecs_to_ms(self):
        assert parse("17 msecs") == 17

    def test_should_convert_sec_to_ms(self):
        assert parse("1 sec") == 1000

    def test_should_convert_from_min_to_ms(self):
        assert parse("1 min") == 60000

    def test_should_convert_from_hr_to_ms(self):
        assert parse("1 hr") == 3600000

    def test_should_convert_days_to_ms(self):
        assert parse("2 days") == 172800000

    def test_should_convert_weeks_to_ms(self):
        assert parse("1 week") == 604800000

    def test_should_convert_months_to_ms(self):
        assert parse("1 month") == 2629800000

    def test_should_convert_years_to_ms(self):
        assert parse("1 year") == 31557600000

    def test_parse_long_string_should_work_with_decimals(self):
        assert parse("1.5 hours") == 5400000

    def test_should_work_with_negative_integers(self):
        assert parse("-100 milliseconds") == -100

    def test_should_work_with_negative_decimals(self):
        assert parse("-1.5 hours") == -5400000

    def test_should_work_with_negative_decimals_starting_with_dot(self):
        assert parse("-.5 hr") == -1800000


class TestParseInvalidInputs:
    def test_should_throw_an_error_when_parse_invalid_input_empty_string(self):
        with pytest.raises(Exception):
            parse("")

    def test_should_throw_an_error_when_parse_invalid_input_length_over_100(self):
        with pytest.raises(Exception):
            parse("\u25b2" * 101)

    def test_should_throw_an_error_when_parse_invalid_input_undefined(self):
        with pytest.raises(Exception):
            parse(None)

    def test_should_throw_an_error_when_parse_invalid_input_null(self):
        with pytest.raises(Exception):
            parse(None)

    def test_should_throw_an_error_when_parse_invalid_input_array(self):
        with pytest.raises(Exception):
            parse([])

    def test_should_throw_an_error_when_parse_invalid_input_object(self):
        with pytest.raises(Exception):
            parse({})

    def test_should_throw_an_error_when_parse_invalid_input_nan(self):
        with pytest.raises(Exception):
            parse(float("nan"))

    def test_should_throw_an_error_when_parse_invalid_input_infinity(self):
        with pytest.raises(Exception):
            parse(float("inf"))

    def test_should_throw_an_error_when_parse_invalid_input_negative_infinity(self):
        with pytest.raises(Exception):
            parse(float("-inf"))

import pytest

from patterns.flyweight.ctypes import (
    c_uint,
    c_ulong,
)


class TestCULong:
    @pytest.mark.parametrize('actual, expected_value', [
        (0, 0),
        (1, 1),
        (-1, 18446744073709551615),

    ])
    def test_is_and_equals(self, actual, expected_value) -> None:
        assert c_ulong(actual) is c_ulong(actual) and (c_ulong(actual).value == expected_value)


class TestCUInt:
    @pytest.mark.parametrize('actual, expected_value', [
        (0, 0),
        (1, 1),
        (-1, 4294967295),
    ])
    def test_is_and_equals(self, actual, expected_value) -> None:
        assert c_uint(actual) is c_uint(actual) and (c_uint(actual).value == expected_value)


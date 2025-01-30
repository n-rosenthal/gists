"""
Unit tests suite for the `gists.src.astro_utils` module.
"""

import datetime;
import pytest;

from typing import Dict, List, Tuple;
from src.astro_utils import Sign;

#   Defines the fixture for the data to be used in the tests
@pytest.fixture
def sign_data() -> List[Tuple[datetime.datetime, Sign]]:
    return [
        (datetime.datetime(2023, 3, 21), Sign.ARIES),
        (datetime.datetime(2024, 3, 30), Sign.ARIES),
        (datetime.datetime(2025, 4, 15), Sign.ARIES),
        (datetime.datetime(2026, 4, 19), Sign.ARIES),
        (datetime.datetime(2027, 4, 20), Sign.TAURUS),
        (datetime.datetime(2028, 4, 25), Sign.TAURUS),
        (datetime.datetime(2029, 5, 1), Sign.TAURUS),
        (datetime.datetime(2030, 5, 19), Sign.TAURUS),
        (datetime.datetime(2031, 5, 20), Sign.GEMINI),
        (datetime.datetime(2032, 5, 26), Sign.GEMINI),
        (datetime.datetime(2033, 6, 1), Sign.GEMINI),
        (datetime.datetime(2034, 6, 19), Sign.GEMINI),
        (datetime.datetime(2035, 6, 21), Sign.CANCER),
        (datetime.datetime(2036, 6, 25), Sign.CANCER),
        (datetime.datetime(2037, 7, 1), Sign.CANCER),
        (datetime.datetime(2038, 7, 19), Sign.CANCER),
        (datetime.datetime(2039, 7, 23), Sign.LEO),
        (datetime.datetime(2040, 7, 26), Sign.LEO),
        (datetime.datetime(2041, 8, 1), Sign.LEO),
        (datetime.datetime(2042, 8, 20), Sign.LEO),
        (datetime.datetime(2043, 8, 23), Sign.VIRGO),
        (datetime.datetime(2044, 8, 27), Sign.VIRGO),
        (datetime.datetime(2045, 9, 1), Sign.VIRGO),
        (datetime.datetime(2046, 9, 19), Sign.VIRGO),
        (datetime.datetime(2047, 9, 23), Sign.LIBRA),
        (datetime.datetime(2048, 9, 26), Sign.LIBRA),
        (datetime.datetime(2049, 10, 1), Sign.LIBRA),
        (datetime.datetime(2050, 10, 20), Sign.LIBRA),
        (datetime.datetime(2051, 10, 22), Sign.LIBRA),
        (datetime.datetime(2052, 10, 27), Sign.SCORPIO),
        (datetime.datetime(2053, 11, 1), Sign.SCORPIO),
        (datetime.datetime(2054, 11, 20), Sign.SCORPIO),
        (datetime.datetime(2055, 11, 22), Sign.SAGITTARIUS),
        (datetime.datetime(2056, 11, 27), Sign.SAGITTARIUS),
        (datetime.datetime(2057, 12, 1), Sign.SAGITTARIUS),
        (datetime.datetime(2058, 12, 21), Sign.SAGITTARIUS),
        (datetime.datetime(2059, 12, 22), Sign.CAPRICORN),
        (datetime.datetime(2060, 12, 27), Sign.CAPRICORN),
        (datetime.datetime(2061, 1, 1), Sign.CAPRICORN),
        (datetime.datetime(2062, 1, 20), Sign.AQUARIUS),
        (datetime.datetime(2063, 1, 21), Sign.AQUARIUS),
        (datetime.datetime(2064, 1, 26), Sign.AQUARIUS),
        (datetime.datetime(2065, 1, 31), Sign.AQUARIUS),
        (datetime.datetime(2066, 2, 19), Sign.PISCES),
        (datetime.datetime(2067, 2, 20), Sign.PISCES),
        (datetime.datetime(2068, 2, 25), Sign.PISCES),
        (datetime.datetime(2069, 3, 1), Sign.PISCES),
        (datetime.datetime(2070, 3, 20), Sign.PISCES),
    ];

#   Tests the `Sign.from_date` method
def test_sign_from_date(sign_data: List[Tuple[datetime.datetime, Sign]]):
    """
    Tests the `Sign.from_date` method.
    """
    for date, sign in sign_data:
        assert Sign.from_date(date) == sign;

if __name__ == "__main__":
    pytest.main(["-v", "astro_utils_tests.py"]);
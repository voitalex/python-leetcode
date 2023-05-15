""" 0013. Roman to Integer """

import pytest
from leetcode.problems.V0000.T0013_roman_to_integer import Solution


@pytest.mark.T0013
@pytest.mark.parametrize(
    'value, expected',
    [
        ('III', 3),
        ('IV', 4),
        ('LVIII', 58),
        ('MCMXCIV', 1994),
    ]
)
def test_roman_to_integer(value, expected):
    assert Solution().romanToInt(value) == expected

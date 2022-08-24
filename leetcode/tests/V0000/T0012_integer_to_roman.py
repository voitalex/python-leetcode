""" 0012. Integer to Roman """

import pytest
from leetcode.problems.V0000.T0012_integer_to_roman import Solution


@pytest.mark.T0012
@pytest.mark.parametrize(
    'value, expected',
    [
        (3, 'III'),
        (4, 'IV'),
        (9, 'IX'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV')
    ]
)
def test_integer_to_roman(value, expected):
    assert Solution().intToRoman(value) == expected

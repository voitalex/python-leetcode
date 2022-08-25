""" 0326. Power of Three """

import pytest
from leetcode.problems.V0300.T0326_power_of_three import Solution


@pytest.mark.T0326
@pytest.mark.parametrize(
    'value, expected',
    [
        (27, True),
        (0, False),
        (9, True),
        (243, True),
        (-3, False),
    ]
)
def test_power_of_three(value, expected):
    assert Solution().isPowerOfThree(value) == expected

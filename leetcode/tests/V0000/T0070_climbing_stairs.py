""" 0070. Climbing Stairs """

import pytest
from leetcode.problems.V0000.T0070_climbing_stairs import Solution


@pytest.mark.T0070
@pytest.mark.parametrize(
    'value, expected',
    [
        (2, 2),
        (3, 3),
    ]
)
def test_climbing_stairs(value, expected):
    assert Solution().climbStairs(value) == expected

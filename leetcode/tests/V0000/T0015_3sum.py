""" 0015. 3Sum """

import pytest
from leetcode.problems.V0000.T0015_3sum import Solution


@pytest.mark.T0015
@pytest.mark.parametrize(
    'value, expected',
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2],[-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]
)
def test_3sum(value, expected):
    assert Solution().threeSum(value) == expected

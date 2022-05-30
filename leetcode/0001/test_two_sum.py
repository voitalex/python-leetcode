""" 0001. Two Sums """

import pytest
from two_sum import Solution


@pytest.mark.t0001
@pytest.mark.parametrize(
    'nums, target, result',
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
)
def test_two_sums(nums, target, result):
    assert Solution().twoSum(nums, target) == result
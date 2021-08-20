""" 0167. Two Sums II - Input Array is Sorted """

import pytest
from leetcode.v0100._0167_two_sums_ii_input_array_is_sorted import Solution


@pytest.mark.t0167
@pytest.mark.parametrize(
    'numbers, target, result',
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
    ]
)
def test_two_sum(numbers, target, result):
    assert Solution().twoSum(numbers, target) == result

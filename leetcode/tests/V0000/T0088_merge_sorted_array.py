""" 0088. Merge Sorted Array """

import pytest
from leetcode.problems.V0000.T0088_merge_sorted_array import Solution


@pytest.mark.T0088
@pytest.mark.parametrize(
    'nums1, m, nums2, n, expected',
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]
)
def test_merge_sorted_array(nums1, m, nums2, n, expected):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected

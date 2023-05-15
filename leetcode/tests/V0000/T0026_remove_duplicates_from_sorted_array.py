""" 0026. Remove Duplicates from Sorted Array """

import pytest
from leetcode.problems.V0000.T0026_remove_duplicates_from_sorted_array import Solution


@pytest.mark.T0026
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),

    ]
)
def test_remove_duplicates_from_sorted_array(value, expected):
    assert Solution().removeDuplicates(value) == expected

""" 0905. Sort Array by Parity """

import pytest
from leetcode.v0900._0905_sort_array_by_parity import Solution


@pytest.mark.t0905
@pytest.mark.parametrize(
    'value, expected',
    [
        ([3,1,2,4], [2,4,3,1]),
        ([0], [0]),
    ]
)
def test_sort_array_by_parity(value, expected):
    assert Solution().sortArrayByParity(value) == expected

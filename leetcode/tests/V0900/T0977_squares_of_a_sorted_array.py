""" 0977. Squares of a Sorted Array """

import pytest
from leetcode.problems.V0900.T0977_squares_of_a_sorted_array import Solution


@pytest.mark.T0977
@pytest.mark.parametrize(
    'value, expected',
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ]
)
def test_squares_of_a_sorted_array(value, expected):
    assert Solution().sortedSquares(value) == expected

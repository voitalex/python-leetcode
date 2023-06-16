""" 0054. Spiral Matrix """

import pytest
from leetcode.problems.V0000.T0054_spiral_matrix import Solution


@pytest.mark.T0054
@pytest.mark.parametrize(
    'value, expected',
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ]
)
def test_spiral_matrix(value, expected):
    assert Solution().spiralOrder(value) == expected

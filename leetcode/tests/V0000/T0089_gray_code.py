""" 0070. Gray Code """

import pytest
from leetcode.problems.V0000.T0089_gray_code import Solution


@pytest.mark.T0089
@pytest.mark.parametrize(
    'value, expected',
    [
        (1, [0, 1]),
        (2, [0, 1, 3, 2]),
        (3, [0, 1, 3, 2, 6, 7, 5, 4])
    ]
)
def test_gray_code(value, expected):
    assert Solution().grayCode(value) == expected


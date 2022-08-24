""" 0069. Sqrt(x) """

import pytest
from leetcode.problems.V0000.T0069_sqrt_x import Solution


@pytest.mark.T0069
@pytest.mark.parametrize(
    'value, expected',
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (4, 2),
        (8, 2),
    ]
)
def test_sqrt_x(value, expected):
    assert Solution().mySqrt(value) == expected

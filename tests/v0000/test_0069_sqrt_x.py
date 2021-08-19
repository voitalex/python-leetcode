""" 0069. Sqrt(x) """

import pytest
from leetcode.v0000._0069_sqrt_x import Solution


@pytest.mark.t0069
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

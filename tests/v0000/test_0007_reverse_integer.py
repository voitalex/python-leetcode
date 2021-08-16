""" 0007. Reverse Integer """


import pytest
from leetcode.v0000._0007_reverse_integer import Solution


@pytest.mark.t0007
@pytest.mark.parametrize(
    'value, expected',
    [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (2**31, 0)
    ]
)
def test_reverse_integer(value, expected):
    assert Solution().reverse(value) == expected

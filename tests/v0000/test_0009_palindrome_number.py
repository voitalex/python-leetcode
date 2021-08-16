""" 0009. Palindrome Number """

import pytest
from leetcode.v0000._0009_palindrome_number import Solution


@pytest.mark.t0009
@pytest.mark.parametrize(
    'value, expected',
    [
        (121, True),
        (-121, False),
        (10, False),
    ]
)
def test_palindrome_number(value, expected):
    assert Solution().isPalindrome(value) == expected

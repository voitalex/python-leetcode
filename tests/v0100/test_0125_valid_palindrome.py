""" 0125. Valid Palindrome """

import pytest
from leetcode.v0100._0125_valid_palindrome import Solution


@pytest.mark.t0125
@pytest.mark.parametrize(
    'value, expected',
    [
        ('A man, a plan, a canal: Panama', True),
        ('race a car', False),
    ]
)
def test_valid_palindrome(value, expected):
    assert Solution().isPalindrome(value) == expected

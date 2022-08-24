""" 0125. Valid Palindrome """

import pytest
from leetcode.problems.V0100.T0125_valid_palindrome import Solution


@pytest.mark.T0125
@pytest.mark.parametrize(
    'value, expected',
    [
        ('A man, a plan, a canal: Panama', True),
        ('race a car', False),
    ]
)
def test_valid_palindrome(value, expected):
    assert Solution().isPalindrome(value) == expected

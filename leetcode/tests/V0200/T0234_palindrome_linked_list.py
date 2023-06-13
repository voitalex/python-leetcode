""" 0234. Palindrome Linked List """

import pytest
from leetcode.problems.V0200.T0234_palindrome_linked_list import ListNode, Solution


@pytest.mark.T0234
@pytest.mark.parametrize(
    'value, expected',
    [
        (ListNode(1, ListNode(2)), False),
        (ListNode(1, ListNode(2, ListNode(2, ListNode(1)))), True),
    ]
)
def test_reverse_linked_list(value, expected):
    assert Solution().isPalindrome(value) == expected


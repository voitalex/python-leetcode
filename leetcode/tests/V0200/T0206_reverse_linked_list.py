""" 0206. Reverse Linked List """

import pytest
from leetcode.problems.V0200.T0206_reverse_linked_list import ListNode, Solution


@pytest.mark.T0206
@pytest.mark.parametrize(
    'value, expected',
    [
        (None, None),
        (
            ListNode(1, ListNode(2)),
            ListNode(2, ListNode(1)),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
        ),
    ]
)
def test_reverse_linked_list(value, expected):

    result = Solution().reverseList(value)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

""" 0092. Reverse Linked List II """

import pytest
from leetcode.problems.V0000.T0092_reverse_linked_list_ii import ListNode, Solution


@pytest.mark.T0092
@pytest.mark.parametrize(
    'head, left, right, expected',
    [
        (ListNode(5), 1, 1, ListNode(5)),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4,
            ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5))))),
        ),
    ]
)
def test_reverse_linked_list(head, left, right, expected):

    result = Solution().reverseBetween(head, left, right)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

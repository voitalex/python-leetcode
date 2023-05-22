""" 0203. Remove Linked List Elements """

import pytest
from leetcode.problems.V0200.T0203_remove_linked_list_elements import ListNode, Solution


@pytest.mark.T0203
@pytest.mark.parametrize(
    'head, val, expected',
    [
        (None, 1, None),
        (
            ListNode(7, ListNode(7, ListNode(7, ListNode(7, )))), 7, None,
        ),
        (
            ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))),
            6,
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ),
    ]
)
def test_reverse_linked_list(head, val, expected):

    result = Solution().removeElements(head, val)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

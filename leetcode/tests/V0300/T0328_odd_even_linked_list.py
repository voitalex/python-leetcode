""" 0328. Odd Even Linked List """

import pytest
from leetcode.problems.V0300.T0328_odd_even_linked_list import ListNode, Solution


@pytest.mark.T0328
@pytest.mark.parametrize(
    'head, expected',
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4))))),
        ),
        (
            ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7))))))),
            ListNode(2, ListNode(3, ListNode(6, ListNode(7, ListNode(1, ListNode(5, ListNode(4))))))),
        ),
    ]
)
def test_odd_even_linked_list(head, expected):

    result = Solution().oddEvenList(head)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

""" 0876. Middle of the Linked List """

import pytest
from leetcode.problems.V0800.T0876_middle_of_the_linked_list import ListNode, Solution


@pytest.mark.T0876
@pytest.mark.parametrize(
    'head, expected',
    [
        (None, None),
        (
                ListNode(1),
                ListNode(1),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(3, ListNode(4, ListNode(5))),
        ),
        (
                ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))),
                ListNode(4, ListNode(5, ListNode(6))),
        ),
    ]
)
def test_middle_of_the_linked_list(head, expected):

    result = Solution().middleNode(head)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

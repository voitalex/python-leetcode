""" 0019. Remove Nth Node From End of List """

import pytest
from leetcode.problems.V0000.T0019_remove_nth_node_from_end_of_list import ListNode, Solution

@pytest.mark.T0019
@pytest.mark.parametrize(
    'value, n, expected',
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (
            ListNode(1), 1,
            None,
        ),
        (
            ListNode(1, ListNode(2)), 1,
            ListNode(1),
        ),
    ]
)
def test_remove_nth_node_from_end_of_list(value, n, expected):

    result = Solution().removeNthFromEnd(value, n)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

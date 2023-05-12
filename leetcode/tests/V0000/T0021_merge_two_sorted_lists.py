""" 0021. Merge Two Sorted Lists """

import pytest
from leetcode.problems.V0000.T0021_merge_two_sorted_lists import ListNode, Solution


@pytest.mark.T0021
@pytest.mark.parametrize(
    'l1, l2, expected',
    [
        (None, None, None),
        (None, ListNode(0), ListNode(0)),
        (
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))),
        ),
    ]
)
def test_valid_parentheses(l1, l2, expected):

    result = Solution().mergeTwoLists(l1, l2)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None


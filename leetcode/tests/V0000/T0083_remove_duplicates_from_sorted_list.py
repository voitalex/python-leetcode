""" 0083. Remove Duplicates from Sorted List """

import pytest
from leetcode.problems.V0000.T0083_remove_duplicates_from_sorted_list import ListNode, Solution


@pytest.mark.T0083
@pytest.mark.parametrize(
    'value, expected',
    [
        (
                ListNode(1, ListNode(1, ListNode(2))),
                ListNode(1, ListNode(2)),
        ),
        (
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))),
            ListNode(1, ListNode(2, ListNode(3))),
        ),
    ]
)
def test_remove_duplicates_from_sorted_list(value, expected):

    result = Solution().deleteDuplicates(value)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

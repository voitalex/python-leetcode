""" 0148. Sort List """

import pytest
from leetcode.problems.V0100.T0148_sort_list import ListNode, Solution


@pytest.mark.T0148
@pytest.mark.parametrize(
    'value, expected',
    [
        (None, None),
        (
            ListNode(4, ListNode(2, ListNode(1, ListNode(3)))),
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        ),
        (
            ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))),
            ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5))))),
        ),
    ]
)
def test_sort_list(value, expected):

    result = Solution().sortList(value)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None


""" 0143. Reorder List """

import pytest
from leetcode.problems.V0100.T0143_reorder_list import ListNode, Solution


@pytest.mark.T0143
@pytest.mark.parametrize(
    'value, expected',
    [
        (None, None),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(1, ListNode(4, ListNode(2, ListNode(3)))),
        ),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3))))),
        ),
    ]
)
def test_reorder_list(value, expected):

    Solution().reorderList(value)
    while value and expected:
        assert value.val == expected.val
        value = value.next
        expected = expected.next

    assert value is None and expected is None

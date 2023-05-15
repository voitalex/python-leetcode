""" 0061. Rotate List """

import pytest
from leetcode.problems.V0000.T0061_rotate_list import ListNode, Solution


@pytest.mark.T0061
@pytest.mark.parametrize(
    'head, k, expected',
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2,
            ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3)))))
        ),
        (
            ListNode(0, ListNode(1, ListNode(2))), 4,
            ListNode(2, ListNode(0, ListNode(1)))
        ),
        (
            ListNode(1, ListNode(2)), 1,
            ListNode(2, ListNode(1))
        ),
    ]
)
def test_rotate_list(head, k, expected):

    result = Solution().rotateRight(head, k)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

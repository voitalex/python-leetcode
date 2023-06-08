""" 0024. Swap Nodes in Pairs
 """

import pytest
from leetcode.problems.V0000.T0024_swap_nodes_in_pairs import ListNode, Solution


@pytest.mark.T0024
@pytest.mark.parametrize(
    'value, expected',
    [
        (None, None),
        (ListNode(1), ListNode(1)),
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
            ListNode(2, ListNode(1, ListNode(4, ListNode(3)))),
        ),
    ]
)
def test_swap_node_in_pairs(value, expected):

    result = Solution().swapPairs(value)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None

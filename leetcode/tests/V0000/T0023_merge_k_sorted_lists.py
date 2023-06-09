""" 0023. Merge K Sorted Lists """

import pytest
from leetcode.problems.V0000.T0023_merge_k_sorted_lists import ListNode, Solution


@pytest.mark.T0023
@pytest.mark.parametrize(
    'lists, expected',
    [
        (None, None),
        ([], None),
        (
            [
                ListNode(1, ListNode(4, ListNode(5))),
                ListNode(1, ListNode(3, ListNode(4))),
                ListNode(2, ListNode(6)),
            ],
            ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
        ),
    ]
)
def test_merge_k_sorted_lists(lists, expected):

    result = Solution().mergeKLists(lists)
    while result and expected:
        assert result.val == expected.val
        result = result.next
        expected = expected.next

    assert result is None and expected is None


""" 0109. Convert Sorted List to Binary Search Tree """

import pytest
from leetcode.problems.V0100.T0109_convert_sorted_list_to_binary_search_tree import ListNode, Solution, TreeNode


@pytest.mark.T0109
@pytest.mark.parametrize(
    'value, expected',
    [
        (None, None),
        (
            ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9))))),
            TreeNode(0, TreeNode(-10, None, TreeNode(-3)), TreeNode(5, None, TreeNode(9))),
        ),
    ]
)
def test_convert_sorted_list_to_binary_search_tree(value, expected):

    def compare(first, second):

        if first is None and second is None:
            return True

        if first is not None and second is not None:
            return first.val == second.val \
                and compare(first.left, second.left) \
                and compare(first.right, second.right)

        return False

    assert compare(Solution().sortedListToBST(value), expected) is True

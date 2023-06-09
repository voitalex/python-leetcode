""" 0108. Convert Sorted Array to Binary Search Tree """

import pytest
from leetcode.problems.V0100.T0108_convert_sorted_array_to_binary_search_tree import Solution, TreeNode


@pytest.mark.T0108
@pytest.mark.parametrize(
    'value, expected',
    [
        (
            [-10, -3, 0, 5, 9],
            TreeNode(0, TreeNode(-10, None, TreeNode(-3)), TreeNode(5, None, TreeNode(9))),
        ),
        (
            [1, 3],
            TreeNode(1, None, TreeNode(3))
        ),
    ]
)
def test_convert_sorted_array_to_binary_search_tree(value, expected):

    def compare(first, second):

        if first is None and second is None:
            return True

        if first is not None and second is not None:
            return first.val == second.val \
                and compare(first.left, second.left) \
                and compare(first.right, second.right)

        return False

    assert compare(Solution().sortedArrayToBST(value), expected) is True

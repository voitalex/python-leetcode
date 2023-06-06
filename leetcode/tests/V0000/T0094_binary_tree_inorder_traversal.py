""" 0094. Binary Tree Inorder Traversal """

import pytest
from leetcode.problems.V0000.T0094_binary_tree_inorder_traversal import Solution, TreeNode


@pytest.mark.T0094
@pytest.mark.parametrize(
    'value, expected',
    [
        (TreeNode(1, None, TreeNode(2, TreeNode(3), None)), [1, 3, 2]),
        (None, []),
        (TreeNode(1), [1]),
    ]
)
def test_binary_tree_inorder_traversal(value, expected):
    assert Solution().inorderTraversal(value) == expected

""" 0144. Binary Tree Preorder Traversal """

import pytest
from leetcode.problems.V0100.T0144_binary_tree_preorder_traversal import Solution, TreeNode


@pytest.mark.T0144
@pytest.mark.parametrize(
    'value, expected',
    [
        (TreeNode(1, None, TreeNode(2, TreeNode(3), None)), [1, 2, 3]),
        (None, []),
        (TreeNode(1), [1]),
    ]
)
def test_binary_tree_preorder_traversal(value, expected):
    assert Solution().preorderTraversal(value) == expected

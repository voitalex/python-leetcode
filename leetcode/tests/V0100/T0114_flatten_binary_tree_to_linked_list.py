""" 0114. Flatten Binary Tree to Linked List """

import pytest
from leetcode.problems.V0100.T0114_flatten_binary_tree_to_linked_list import Solution, TreeNode


@pytest.mark.T0114
@pytest.mark.parametrize(
    'value, expected',
    [
        (
            TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))),
            TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))),

        ),
        (None, None),
        (TreeNode(0), TreeNode(0)),
    ]
)
def test_flatten_binary_tree_to_linked_list(value, expected):

    Solution().flatten(value)
    while expected and value:

        assert value.val == expected.val

        value = value.right
        expected = expected.right

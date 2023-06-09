""" 0110. Balanced Binary Tree """

import pytest
from leetcode.problems.V0100.T0110_balanced_binary_tree import Solution, TreeNode


@pytest.mark.T0110
@pytest.mark.parametrize(
    'value, expected',
    [
        (None, True),
        (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), True),
        (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2)), False),
    ]
)
def test_balanced_binary_tree(value, expected):
    assert Solution().isBalanced(value) == expected

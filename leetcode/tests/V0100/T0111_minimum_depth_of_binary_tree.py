""" 0111. Minimum Depth of Binary Tree """

import pytest
from leetcode.problems.V0100.T0111_minimum_depth_of_binary_tree import Solution, TreeNode


@pytest.mark.T0111
@pytest.mark.parametrize(
    'value, expected',
    [
        (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 2),
        (TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))), 5),
        (None, 0),
    ]
)
def test_minimum_depth_of_binary_tree(value, expected):
    assert Solution().minDepth(value) == expected

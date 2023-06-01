""" 0104. Maximum Depth of Binary Tree """

import pytest
from leetcode.problems.V0100.T0104_maximum_depth_of_binary_tree import Solution, TreeNode


@pytest.mark.T0104
@pytest.mark.parametrize(
    'value, expected',
    [
        (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 3),
        (TreeNode(1, None, TreeNode(2)), 2),
        (None, 0),
        (TreeNode(0), 1),
    ]
)
def test_maximum_depth_of_binary_tree(value, expected):
    assert Solution().maxDepth(value) == expected

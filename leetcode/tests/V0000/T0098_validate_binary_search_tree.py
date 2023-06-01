""" 0098. Validate Binary Search Tree """

import pytest
from leetcode.problems.V0000.T0098_validate_binary_search_tree import Solution, TreeNode


@pytest.mark.T0098
@pytest.mark.parametrize(
    'value, expected',
    [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    ]
)
def test_validate_binary_search_tree(value, expected):
    assert Solution().isValidBST(value) == expected

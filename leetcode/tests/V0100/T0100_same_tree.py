""" 0100. Same Tree """

import pytest
from leetcode.problems.V0100.T0100_same_tree import Solution, TreeNode


@pytest.mark.T0100
@pytest.mark.parametrize(
    'first, second, expected',
    [
        (
            TreeNode(1, TreeNode(2), TreeNode(3)),
            TreeNode(1, TreeNode(2), TreeNode(3)),
            True,
        ),
        (
            TreeNode(1, TreeNode(2)),
            TreeNode(1, None, TreeNode(2)),
            False,
        ),
        (
            TreeNode(1, TreeNode(2), TreeNode(1)),
            TreeNode(1, TreeNode(1), TreeNode(2)),
            False,
        ),
    ]
)
def test_same_tree(first, second, expected):
    assert Solution().isSameTree(first, second) == expected

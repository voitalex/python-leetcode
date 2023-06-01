""" 0104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down
to the farthest leaf node.

Example 1:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 3

Example 2:
    Input: root = [1, null, 2]
    Output: 2

Example 3:
    Input: root = []
    Output: 0

Example 4:
    Input: root = [0]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [0, 10^4].
    -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    """ Узел дерева """

    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val: int = val
        self.left: Optional['TreeNode'] = left
        self.right: Optional['TreeNode'] = right

    def __str__(self) -> str:
        """ Возвращает узел дерева в строковом представлении """
        return str(self.val)


class Solution:
    """ Maximum Depth of Binary Tree """

    def traverse(self, root: Optional[TreeNode]) -> int:
        """ Возвращает глубину дерева до указанного узла """

        if root is None:
            return 0

        return max(self.traverse(root.left) + 1, self.traverse(root.right) + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ Решение задачи """
        return self.traverse(root)



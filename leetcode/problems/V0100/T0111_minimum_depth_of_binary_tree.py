""" 0111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
    Input: root = [3, 9, 20, null, null, 15, 7]
    Output: 2

Example 2:
    Input: root = [2, null, 3, null, 4, null, 5, null, 6]
    Output: 5

Constraints:
  * The number of nodes in the tree is in the range [0, 10^5].
  * -1000 <= Node.val <= 1000
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
    """ Minimum Depth of Binary Tree """

    def traverse(self, root: Optional[TreeNode]) -> int:
        """ Возвращает глубину дерева до указанного узла """

        if root is None:
            return 0

        return min(self.traverse(root.left) + 1, self.traverse(root.right) + 1)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """ Решение задачи """

        if root is None:
            return 0

        if root.left is None:
            return self.minDepth(root.right) + 1

        if root.right is None:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

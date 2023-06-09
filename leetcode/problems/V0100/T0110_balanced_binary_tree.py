""" 0110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

Example 2:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

Example 3:
    Input: root = []
    Output: true

Constraints:
  * The number of nodes in the tree is in the range [0, 5000].
  * -10^4 <= Node.val <= 10^4
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
    """ Balanced Binary Tree """

    def max_depth(self, root: Optional[TreeNode]) -> int:
        """ Возвращают глубину дерева от указанного узла """

        if root is None:
            return 0

        # Значение -1 указывает, что дерево не сбалансировано

        left_height = self.max_depth(root.left)
        if left_height == -1:
            return -1

        right_height = self.max_depth(root.right)
        if right_height == -1:
            return -1

        return max(left_height, right_height) + 1 if abs(left_height - right_height) <= 1 else -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """ Решение задачи """
        return self.max_depth(root) != -1

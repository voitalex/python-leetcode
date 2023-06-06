""" 0094. Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,3,2]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Example 4:
    Input: root = [1,2]
    Output: [2,1]

Example 5:
    Input: root = [1,null,2]
    Output: [1,2]

Constraints:
  * The number of nodes in the tree is in the range [0, 100].
  * -100 <= Node.val <= 100
"""

from collections import deque
from typing import List, Optional, Iterable


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
    """ Binary Tree Inorder Traversal """

    def traverse(self, root: Optional[TreeNode]) -> Iterable[int]:
        """ Обход всех узлов """

        if not root:
            return

        yield from self.traverse(root.left)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Решение задачи """

        if root is None:
            return []

        result = []
        stack = deque()

        node = root
        while stack or node:

            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result

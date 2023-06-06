""" 0144. Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
    Input: root = [1,null,2,3]
    Output: [1,2,3]

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [1]
    Output: [1]

Constraints:
  * The number of nodes in the tree is in the range [0, 100].
  * -100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional, List


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
    """ Binary Tree Preorder Traversal """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ Решение задачи """

        if root is None:
            return []

        result = []
        stack = deque()

        stack.append(root)
        while stack:

            node: Optional[TreeNode] = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result

print(Solution().preorderTraversal(
    TreeNode(1, None, TreeNode(2, TreeNode(3), None))
))





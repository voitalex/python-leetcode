""" 0114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":
  * The "linked list" should use the same TreeNode class where the right child pointer points to the next node
    in the list and the left child pointer is always null.
  * The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

            1
          /  \
        2     5        =>    1 - 2 - 3 - 4 - 5 - 6
      /  \     \
    3     4     6

Example 2:
    Input: root = []
    Output: []

Example 3:
    Input: root = [0]
    Output: [0]

Constraints:
  * The number of nodes in the tree is in the range [0, 2000].
  * -100 <= Node.val <= 100
"""

from collections import deque
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
    """ Flatten Binary Tree to Linked List """

    def flatten(self, root: Optional[TreeNode]) -> None:
        """ Решение задачи """

        stack = deque()
        node = root

        while node or stack:

            if node.right:
                stack.append(node.right)

            if node.left:
                node.right = node.left
                node.left = None
            elif stack:
                temp = stack.pop()
                node.right = temp

            node = node.right

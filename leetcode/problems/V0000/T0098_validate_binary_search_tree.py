""" 0098. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
  * The left subtree of a node contains only nodes with keys less than the node's key.
  * The right subtree of a node contains only nodes with keys greater than the node's key.
  * Both the left and right subtrees must also be binary search trees.

Example 1:
    Input: root = [2,1,3]
    Output: true

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
  * The number of nodes in the tree is in the range [1, 10^4].
  * -2^31 <= Node.val <= 2^31 - 1
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
    """ Validate Binary Search Tree """

    def traverse(self, root: Optional[TreeNode], low: Optional[int], high: Optional[int]) -> bool:
        """ Возвращает True если указанный узел образует корректное BST """

        if root is None:
            return True

        return (low is None or low < root.val) \
            and (high is None or root.val < high) \
            and self.traverse(root.left, low, root.val) \
            and self.traverse(root.right, root.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ Решение задачи """
        return self.traverse(root, None, None)

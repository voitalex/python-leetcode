""" 0100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

Constraints:
  * The number of nodes in both trees is in the range [0, 100].
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
    """ Same Tree """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """ Решение задачи """

        if p is None and q is None:
            return True

        if p is not None and q is not None:
            return p.val == q.val \
                and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)

        return False


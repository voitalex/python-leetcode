""" 0101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:

    Input: root = [1,2,2,3,4,4,3]
    Output: true

              1
           /    \
         2       2
       /  \    /  \
     3    4   4   3

Example 2:

    Input: root = [1,2,2,null,3,null,3]
    Output: false

            1
         /    \
       2       2
        \       \
         3       3

Constraints:
  * The number of nodes in the tree is in the range [1, 1000].
  * -100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    """ Узел дерева """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ Symmetric Tree """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """ Решение задачи """


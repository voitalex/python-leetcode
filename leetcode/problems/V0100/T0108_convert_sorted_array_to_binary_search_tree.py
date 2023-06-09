""" 0108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
    Input: nums = [1,3]
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
  * 1 <= nums.length <= 10^4
  * -10^4 <= nums[i] <= 10^4
  * nums is sorted in a strictly increasing order.
"""

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
    """ Convert Sorted Array to Binary Search Tree """

    def create_node(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        """ Возвращает новый узел дерева с потомками """

        if left > right:
            return None

        middle = (right + left) // 2

        node = TreeNode(nums[middle])
        node.left = self.create_node(nums, left, middle - 1)
        node.right = self.create_node(nums, middle + 1, right)

        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """ Решение задачи """
        return self.create_node(nums, 0, len(nums) - 1)

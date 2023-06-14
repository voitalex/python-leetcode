""" 0109. Convert Sorted List to Binary Search Tree

Given the head of a singly linked list where elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

Example 1:
    Input: head = [-10, -3, 0, 5, 9]
    Output: [0, -3, 9, -10, null, 5]
    Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:
    Input: head = []
    Output: []

Constraints:
  * The number of nodes in head is in the range [0, 2 * 10^4].
  * -10^5 <= Node.val <= 10^5
"""

from typing import Optional


class ListNode:
    """ Элемент списка """

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


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
    """ Convert Sorted List to Binary Search Tree """

    head: Optional[ListNode] = None

    @staticmethod
    def length(head: Optional[ListNode]) -> int:
        """ Возвращает длину списка """
        result = 0
        while head:
            result += 1
            head = head.next
        return result

    def traverse(self, start: int, end: int) -> Optional[TreeNode]:
        """ Создание дерева на основе связанного списка """

        if start > end:
            return None

        middle = (start + end) // 2
        left_child = self.traverse(start, middle - 1)
        parent = TreeNode(self.head.val, left_child)

        self.head = self.head.next
        parent.right = self.traverse(middle + 1, end)

        return parent

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """ Решение задачи """
        self.head = head
        return self.traverse(0, self.length(head) - 1)

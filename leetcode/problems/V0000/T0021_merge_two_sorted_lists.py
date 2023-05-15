""" 0021. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together
the nodes of the first two lists.

Example 1:
    Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
    Output: [1, 1, 2, 3, 4, 4]

Example 2:
    Input: l1 = [], l2 = []
    Output: []

Example 3:
    Input: l1 = [], l2 = [0]
    Output: [0]

Constraints:
  * The number of nodes in both lists is in the range [0, 50].
  * -100 <= Node.val <= 100
  * Both l1 and l2 are sorted in non-decreasing order.
"""

from typing import Optional


class ListNode:
    """ Элемент списка """

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next = next


class Solution:
    """ Merge Two Sorted Lists """

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        result = ListNode(0)
        result_iter = result
        l1_iter, l2_iter = l1, l2
        while l1_iter or l2_iter:

            if l1_iter and l2_iter:

                if l1_iter.val <= l2_iter.val:
                    node = l1_iter
                    l1_iter =  l1_iter.next
                else:
                    node = l2_iter
                    l2_iter =  l2_iter.next

                result_iter.next = node
                result_iter = node

            elif l1_iter:
                result_iter.next = l1_iter
                l1_iter = None

            else:
                result_iter.next = l2_iter
                l2_iter = None

        return result.next

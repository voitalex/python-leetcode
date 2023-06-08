""" 0024. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]

Constraints:
  * The number of nodes in the list is in the range [0, 100].
  * 0 <= Node.val <= 100
"""

from typing import Optional


class ListNode:
    """ Элемент списка """

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    """ Swap Nodes in Pairs """

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:
            next, next_next = current.next, current.next.next
            prev.next = next
            next.next = current
            current.next = next_next
            prev = current
            current = next_next

        return dummy.next

""" 0206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

Example 2:
    Input: head = [1,2]
    Output: [2,1]

Example 3:
    Input: head = []
    Output: []

Constraints:
  * The number of nodes in the list is the range [0, 5000].
  * -5000 <= Node.val <= 5000
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
    """ Reverse Linked List """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        if head is None or head.next is None:
            return head

        result = ListNode(head.val)
        rest = head.next
        while rest:
            temp = rest.next
            rest.next = result
            result = rest
            rest = temp

        return result

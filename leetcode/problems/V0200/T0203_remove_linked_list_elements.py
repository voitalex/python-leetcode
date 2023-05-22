""" 0203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]

Example 2:
    Input: head = [], val = 1
    Output: []

Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []


Constraints:
  * The number of nodes in the list is in the range [0, 104].
  * 1 <= Node.val <= 50
  * 0 <= val <= 50
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
    """ Remove Linked List Elements """

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """ Решение задачи """

        iter = ListNode(0, head)
        result = iter

        while iter.next:

            if iter.next.val == val:
                iter.next = iter.next.next
            else:
                iter = iter.next

        return result.next

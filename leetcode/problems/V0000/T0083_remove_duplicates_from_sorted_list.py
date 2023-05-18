""" 0083. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:
    Input: head = [1,1,2]
    Output: [1,2]

Example 2:
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]

Constraints:
  * The number of nodes in the list is in the range [0, 300].
  * -100 <= Node.val <= 100
  * The list is guaranteed to be sorted in ascending order.
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
    """ Remove Duplicates from Sorted List """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        if head is None or head.next is None:
            return head

        result = head
        rest = head.next
        while rest:

            if head.val == rest.val:
                head.next = rest.next
            else:
                head = head.next

            rest = rest.next

        return result


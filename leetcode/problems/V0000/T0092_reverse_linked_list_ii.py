""" 0092. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5], left = 2, right = 4
    Output: [1,4,3,2,5]

Example 2:
    Input: head = [5], left = 1, right = 1
    Output: [5]

Constraints:
  * The number of nodes in the list is n.
  * 1 <= n <= 500
  * -500 <= Node.val <= 500
  * 1 <= left <= right <= n
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
    """ Reverse Linked List II """

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ Решение задачи """

        if head is None or head.next is None or left == right:
            return head

        dummy_head = ListNode(0, head)

        # Продвижение по списку до начала рассматриваемого участка
        before = dummy_head
        for _ in range(left - 1):
            before = before.next

        sublist_head = before.next
        sublist = sublist_head
        sublist_rest = sublist.next
        for _ in range(left, right):
            temp = sublist_rest.next
            sublist_rest.next = sublist
            sublist = sublist_rest
            sublist_rest = temp

        sublist_head.next = sublist_rest
        before.next = sublist

        return dummy_head.next

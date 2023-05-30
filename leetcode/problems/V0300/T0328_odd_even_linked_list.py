""" 0328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together
followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

Example 2:
    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]

Constraints:
  * The number of nodes in the linked list is in the range [0, 104].
  * -10^6 <= Node.val <= 10^6
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
    """ Odd Even Linked List """

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        if head is None:
            return head

        even_head, odd_head = ListNode(0), ListNode(0)
        tails = {False: odd_head, True: even_head}
        turn = False
        while head is not None:
            tails[turn].next = head
            tails[turn] = tails[turn].next
            head = head.next
            turn = not turn

        tails[True].next = None
        tails[False].next = even_head.next

        return odd_head.next

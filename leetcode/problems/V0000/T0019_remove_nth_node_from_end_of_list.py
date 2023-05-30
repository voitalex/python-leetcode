""" 0019. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1, 2, 3, 4, 5], n = 2
    Output: [1, 2, 3, 5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1, 2], n = 1
    Output: [1]

Constraints:
  * The number of nodes in the list is sz.
  * 1 <= sz <= 30
  * 0 <= Node.val <= 100
  * 1 <= n <= sz
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
    """ Remove Nth Node From End of List """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ Решение задачи """

        # Воспользуемся двумя итераторами:
        #  - первый итератор передвинем на N шагов вперед
        #  - второй итератор оставим на месте
        # Далее, как только первый итератор достигнет хвоста списка, второй укажет на удаляемый элемент

        dummy_head = ListNode(0, head)

        first = dummy_head.next
        for _ in range(n):
            first = first.next

        second = dummy_head
        while first is not None:
            second = second.next
            first = first.next

        second.next = second.next.next

        return dummy_head.next

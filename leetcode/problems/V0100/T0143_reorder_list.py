"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

    L0 -> L1 -> . . .  -> Ln - 1 -> Ln

Reorder the list to be on the following form:

    L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
    Input: head = [1,2,3,4]
    Output: [1,4,2,3]

Example 2:
    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
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
    """ Reorder List """

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Возвращает перевернутый связанный список """

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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """ Решение задачи """

        if head is None or head.next is None:
            return head

        # Нахождение второй половины списка
        slow, fast = head, head
        while fast is not None and fast.next is not None and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        first, second = head, self.reverse(second)
        while second:

            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2

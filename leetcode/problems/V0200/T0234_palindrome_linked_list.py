""" 0234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
    Input: head = [1,2,2,1]
    Output: true

Example 2:
    Input: head = [1,2]
    Output: false

Constraints:
  * The number of nodes in the list is in the range [1, 10^5].
  * 0 <= Node.val <= 9
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
    """ Palindrome Linked List """

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """ Решение задачи """

        # Нахождение второй половины списка
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Сравнение первой половины с перевернутой второй половиной списка
        first_half, second_half = head, self.reverse(slow)
        while first_half and second_half:

            if first_half.val != second_half.val:
                return False

            first_half = first_half.next
            second_half = second_half.next

        return True

""" 0148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

Example 3:
    Input: head = []
    Output: []

Constraints:
  * The number of nodes in the list is in the range [0, 5 * 10^4].
  * -10^5 <= Node.val <= 10^5
"""

from typing import Optional, Tuple


class ListNode:
    """ Элемент списка """

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    """ Sort List """

    @staticmethod
    def count(head: ListNode) -> int:
        """ Возвращает количество элементов в списке """
        result = 0
        while head:
            result += 1
            head = head.next
        return result

    def divide(self, head: ListNode) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        """ Разделение списка на две равные части """

        count = self.count(head)

        middle, count_middle = count // 2, 0
        node, left, right = head, head, None
        while node:

            count_middle += 1
            next = node.next

            if count_middle == middle:
                node.next = None
                right = next

            node = node.next

        return left, right

    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> ListNode:
        """ Возвращает объединенный список """

        result = ListNode(0)
        result_iter = result
        left_iter, right_iter = left, right
        while left_iter or right_iter:

            if left_iter and right_iter:

                if left_iter.val <= right_iter.val:
                    node = left_iter
                    left_iter =  left_iter.next
                else:
                    node = right_iter
                    right_iter =  right_iter.next

                result_iter.next = node
                result_iter = node

            elif left_iter:
                result_iter.next = left_iter
                left_iter = None

            else:
                result_iter.next = right_iter
                right_iter = None

        return result.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        # Для сортировки списка следует:
        #  * разбить список на два подсписка
        #  * отсортировать каждый из подсписков
        #  * объединить два подсписка

        if head is None or head.next is None:
            return head

        left, right = self.divide(head)

        h1 = self.sortList(left)
        h2 = self.sortList(right)

        merged = self.merge(h1, h2)

        return merged

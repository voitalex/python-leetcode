""" 0061. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]

                1 -> 2 -> 3 -> 4 -> 5
    rotate 1:   5 -> 1 -> 2 -> 3 -> 4
    rotate 2:   4 -> 5 -> 1 -> 2 -> 3

Example 2:

    Input: head = [0,1,2], k = 4
    Output: [2,0,1]

                0 -> 1 -> 2
    rotate 1:   2 -> 0 -> 1
    rotate 2:   1 -> 2 -> 0
    rotate 3:   0 -> 1 -> 2
    rotate 4:   2 -> 0 -> 1

Constraints:
  * The number of nodes in the list is in the range [0, 500].
  * -100 <= Node.val <= 100
  * 0 <= k <= 2 * 10^9
"""

from typing import Optional


class ListNode:
    """ Элемент связанного списка """

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    """ Rotate List """

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ Решение задачи """

        if not head:
            return head

        # Поиск длины связанного списка и его последнего элемента
        length, tail = 1, head
        while tail.next:
            length += 1
            tail = tail.next

        rotations = k % length
        if not rotations:
            return head

        # Определение границ сдвигаемых групп элементов
        #
        # Перед сдвигом элементов на k позицией (на примере k=3):
        #
        #       N1 --> N2 --> N3 --> N4 --> N5
        #       |------|      |-------------|
        #    r_head  r_tail  l_head      l_tail
        #
        # После сдвига элементов:
        #
        #       N3 --> N4 --> N5 --> N1 --> N2
        #       |-------------|      |------|
        #     l_head       l_tail  r_head  r_tail

        l_length, l_tail = rotations, tail
        r_length, r_head = length - rotations, head

        r_tail = r_head
        for _ in range(r_length - 1):
            r_tail = r_tail.next

        l_head = r_tail.next

        l_tail.next = r_head
        r_tail.next = None

        return l_head

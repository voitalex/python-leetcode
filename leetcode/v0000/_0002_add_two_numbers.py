""" 0002. Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored
in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as
a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9

It is guaranteed that the list represents a number that does not have leading zeros.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class ListNode:
    """ Однонаправленный связанный список """
    val: int
    next: Optional['ListNode'] = None


class Solution:
    """ Add Two Numbers """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ Решение задачи """

        def num_from_list(lst: ListNode) -> int:
            """ Возвращает число, собранное из значений элементов списка """
            digits: List[int] = []
            current: Optional[ListNode] = lst
            while current:
                digits.append(current.val)
                current = current.next
            return int(''.join(str(digit) for digit in digits[::-1]))

        def list_from_num(val: int) -> ListNode:
            """ Возвращает список, сформированный из цифр указанного числа """

            digits = [int(ch) for ch in list(str(val))]
            result = ListNode(digits[0])
            for digit in digits[1:]:
                result = ListNode(digit, result)
            return result

        first, second = num_from_list(l1), num_from_list(l2)
        return list_from_num(first + second)

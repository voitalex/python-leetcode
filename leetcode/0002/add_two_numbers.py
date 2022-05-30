""" 0002. Add Two Numbers """

from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class ListNode:
    """ Однонаправленный связанный список """
    value: int
    next: Optional['ListNode'] = None


class Solution:
    """ Add Two Numbers """

    @staticmethod
    def convert_linked_list_to_number(lst: ListNode) -> int:
        """ Возвращает целочисленное значение на основе значений связанного списка """

        digits: List[int] = []
        current: Optional[ListNode] = lst
        while current:
            digits.append(current.value)
            current = current.next
        return int(''.join(str(digit) for digit in digits[::-1]))

    @staticmethod
    def convert_number_to_linked_list(value: int) -> ListNode:
        """ Возвращает целочисленное значение на основе значений связанного списка """

        digits = [int(ch) for ch in list(str(value))]
        result = ListNode(digits[0])
        for digit in digits[1:]:
            result = ListNode(digit, result)

        return result

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ Решение задачи """

        first, second = self.convert_linked_list_to_number(l1), self.convert_linked_list_to_number(l2)
        return self.convert_number_to_linked_list(first + second)

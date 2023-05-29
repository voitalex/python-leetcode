""" 0160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

        a1 -- a2
                \
                 c1 -- c2 -- c3
                /
  b1 -- b2 -- b3

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
    Output: Intersected at '8'

Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
    Output: Intersected at '2'

Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
    Output: No intersection

Constraints:
  * The number of nodes of listA is in the m.
  * The number of nodes of listB is in the n.
  * 1 <= m, n <= 3 * 10^4
  * 1 <= Node.val <= 10^5
  * 0 <= skipA < m
  * 0 <= skipB < n
  * intersectVal is 0 if listA and listB do not intersect.
  * intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
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
    """ Intersection of Two Linked Lists """

    def advance(self, head: ListNode, k: int) -> Optional[ListNode]:
        """ Перемещение головы списка на k элементов вперед """
        for _ in range(k):
            head = head.next
        return head

    def length(self, head: Optional[ListNode]) -> int:
        """ Возвращает длину списка """
        result = 0
        while head:
            head = head.next
            result += 1
        return result

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """ Решение задачи """

        if headA is None or headB is None:
            return None

        head_a, head_b = headA, headB
        len_a, len_b = self.length(head_a), self.length(head_b)

        # Перемещение головы длинного списка для выравнивания длин списков
        if len_a > len_b:
            head_a = self.advance(head_a, len_a - len_b)
        else:
            head_b = self.advance(head_b, len_b - len_a)

        while head_a is not None and head_b is not None and head_a != head_b:
            head_a = head_a.next
            head_b = head_b.next

        return head_a

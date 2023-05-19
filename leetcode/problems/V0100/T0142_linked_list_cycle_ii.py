""" 0142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.

Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
    Input: head = [3,2,0,-4], pos = 1
    Output: tail connects to node index 1
    Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
    Input: head = [1,2], pos = 0
    Output: tail connects to node index 0
    Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
    Input: head = [1], pos = -1
    Output: no cycle
    Explanation: There is no cycle in the linked list.

Constraints:
  * The number of the nodes in the list is in the range [0, 104].
  * -10^5 <= Node.val <= 10^5
  * pos is -1 or a valid index in the linked-list.
"""

from typing import Optional


class ListNode:
    """ Элемент списка """

    def __init__(self, val: int, next: Optional['ListNode'] = None):
        self.val: int = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    """ Linked List Cycle II """

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        fast_iter = slow_iter = head
        while fast_iter and fast_iter.next:

            slow_iter = slow_iter.next
            fast_iter = fast_iter.next.next

            # Обнаружен цикл. Находим стартовый узел цикла
            if slow_iter == fast_iter:

                slow_iter = head
                while slow_iter != fast_iter:
                    slow_iter = slow_iter.next
                    fast_iter = fast_iter.next

                return slow_iter

        return None

repeated = ListNode(2)
repeated.next = ListNode(0, ListNode(-4, repeated))
head = ListNode(3, repeated)
t = Solution().detectCycle(head)
print(t)

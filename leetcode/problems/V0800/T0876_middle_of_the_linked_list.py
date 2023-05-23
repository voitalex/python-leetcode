""" 0876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example 2:
    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
  * The number of nodes in the list is in the range [1, 100].
  * 1 <= Node.val <= 100
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
    """ Middle of the Linked List """

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Решение задачи """

        move = False
        iter = result = head
        while iter:

            iter = iter.next
            if move:
                result = result.next

            move = not move

        return result

print(
    Solution().middleNode(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    )
)
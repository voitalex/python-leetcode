""" 0138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer,
which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes,
where each new node has its value set to the value of its corresponding original node.
Both the next and random pointer of the new nodes should point to new nodes in the copied list
such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented
as a pair of [val, random_index] where:
  * val: an integer representing Node.val
  * random_index: the index of the node (range from 0 to n-1) that the random pointer points to,
    or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:
    Input: head = [ [7,null], [13,0], [11,4], [10,2], [1,0] ]
    Output: [ [7,null], [13,0], [11,4], [10,2], [1,0] ]

Example 2:
    Input: head = [ [1,1], [2,1] ]
    Output: [ [1,1], [2,1] ]

Example 3:
    Input: head = [ [3,null], [3,0], [3,null] ]
    Output: [ [3,null], [3,0], [3,null] ]

Constraints:
  * 0 <= n <= 1000
  * -10^4 <= Node.val <= 10^4
  * Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional


class Node:
    """ Элемент списка """

    def __init__(self, val: int = 0, next: Optional['Node'] = None, random: 'Node' = None):
        self.val: int = val
        self.next = next
        self.random = random

    def __str__(self) -> str:
        return str(self.val)

class Solution:
    """ Copy List with Random Pointer """

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ Решение задачи """

        # Для создания "глубокой" копии связанного списка следует:
        #   * создать копию каждого узла исходного списка
        #   * установить "random" указатель для скопированных узлов
        #   * восстановить исходный порядок узлов


        node = head
        while node:
            next_node = node.next
            copy = Node(node.val)
            node.next = copy
            copy.next = next_node
            node = next_node

        node = head
        while node:
            node.next.random = node.random.next if node.random else None
            node = node.next.next

        node = head
        head_copy = node.next if node else None
        while node:
            copy = node.next
            node.next = copy.next
            node = node.next
            copy.next = node.next if node else None

        return head_copy

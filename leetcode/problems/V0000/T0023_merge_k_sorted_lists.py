""" 0023. Merge K Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [ [1, 4, 5], [1, 3, 4], [2 ,6] ]
    Output: [1 ,1, 2, 3, 4, 4, 5, 6]
    Explanation: The linked-lists are:
    [
      1 -> 4 -> 5,
      1 -> 3 -> 4,
      2 -> 6
    ] merging them into one sorted list:
    1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: []

Constraints:
  * k == lists.length
  * 0 <= k <= 10^4
  * 0 <= lists[i].length <= 500
  * -10^4 <= lists[i][j] <= 10^4
  * lists[i] is sorted in ascending order.
  * The sum of lists[i].length won't exceed 10^4.
"""

from typing import List, Optional


class ListNode:
    """ Элемент списка """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """ Merge K Sorted Lists """

    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """ Объединение двух списков """

        result = ListNode(0)
        result_iter = result
        l1_iter, l2_iter = l1, l2
        while l1_iter or l2_iter:

            if l1_iter and l2_iter:

                if l1_iter.val <= l2_iter.val:
                    node = l1_iter
                    l1_iter =  l1_iter.next
                else:
                    node = l2_iter
                    l2_iter =  l2_iter.next

                result_iter.next = node
                result_iter = node

            elif l1_iter:
                result_iter.next = l1_iter
                l1_iter = None

            else:
                result_iter.next = l2_iter
                l2_iter = None

        return result.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """ Решение задачи """

        if not lists:
            return None

        end = len(lists) - 1
        while end > 0:

            begin = 0
            while begin < end:
                lists[begin] = self.merge_two_lists(lists[begin], lists[end])
                begin += 1
                end -= 1

        return lists[0]


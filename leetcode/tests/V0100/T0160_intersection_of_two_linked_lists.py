""" 0160. Intersection of Two Linked Lists """

import pytest
from leetcode.problems.V0100.T0160_intersection_of_two_linked_lists import ListNode, Solution


@pytest.mark.T0160
def test_intersection_of_two_linked_lists_01():

    after_intersection = ListNode(4, ListNode(5))
    intersection = ListNode(8, after_intersection)

    head_a = ListNode(4, ListNode(1, intersection))
    head_b = ListNode(5, ListNode(6, ListNode(1, intersection)))

    assert Solution().getIntersectionNode(head_a, head_b) == intersection


@pytest.mark.T0160
def test_intersection_of_two_linked_lists_02():

    intersection = ListNode(4)

    head_a = ListNode(1, ListNode(9, ListNode(1, ListNode(2, intersection))))
    head_b = ListNode(3, ListNode(2, intersection))

    assert Solution().getIntersectionNode(head_a, head_b) == intersection


@pytest.mark.T0160
def test_linked_list_cycle_03():

    head_a = ListNode(2, ListNode(6, ListNode(4)))
    head_b = ListNode(1, ListNode(5))

    assert Solution().getIntersectionNode(head_a, head_b) is None





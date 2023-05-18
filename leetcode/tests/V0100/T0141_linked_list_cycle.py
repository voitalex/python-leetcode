""" 0141. Linked List Cycle """

import pytest
from leetcode.problems.V0100.T0141_linked_list_cycle import ListNode, Solution


@pytest.mark.T0141
def test_linked_list_cycle_01():

    repeated = ListNode(2)
    repeated.next = ListNode(0, ListNode(4, repeated))
    head = ListNode(3, repeated)
    assert Solution().hasCycle(head) is True


@pytest.mark.T0141
def test_linked_list_cycle_02():

    repeated = ListNode(1)
    repeated.next = ListNode(2, repeated)
    head = repeated
    assert Solution().hasCycle(head) is True


@pytest.mark.T0141
def test_linked_list_cycle_03():

    head = ListNode(1)
    assert Solution().hasCycle(head) is False







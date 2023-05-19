""" 0141. Linked List Cycle II"""

import pytest
from leetcode.problems.V0100.T0142_linked_list_cycle_ii import ListNode, Solution


@pytest.mark.T0142
def test_linked_list_cycle_ii_01():

    repeated = ListNode(2)
    repeated.next = ListNode(0, ListNode(-4, repeated))
    head = ListNode(3, repeated)
    assert Solution().detectCycle(head) == repeated


@pytest.mark.T0142
def test_linked_list_cycle_ii_02():

    repeated = ListNode(1)
    repeated.next = ListNode(2, repeated)
    head = repeated
    assert Solution().detectCycle(head) == repeated


@pytest.mark.T0142
def test_linked_list_cycle_ii_03():

    head = ListNode(1)
    assert Solution().detectCycle(head) is None

""" 0237. Delete Node in a Linked List """

import pytest
from leetcode.problems.V0200.T0237_delete_node_in_a_linked_list import ListNode, Solution


@pytest.mark.T0237
def test_delete_node_in_a_linked_list_01():

    node = ListNode(5, ListNode(1, ListNode(9)))
    head = ListNode(4, node)
    expected = ListNode(4, ListNode(1, ListNode(9)))

    Solution().deleteNode(node)
    while head and expected:
        assert head.val == expected.val
        head = head.next
        expected = expected.next

    assert head is None and expected is None


@pytest.mark.T0237
def test_delete_node_in_a_linked_list_02():

    node = ListNode(1, ListNode(9))
    head = ListNode(4, ListNode(5, node))
    expected = ListNode(4, ListNode(5, ListNode(9)))

    Solution().deleteNode(node)
    while head and expected:
        assert head.val == expected.val
        head = head.next
        expected = expected.next

    assert head is None and expected is None

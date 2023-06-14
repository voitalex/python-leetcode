""" 0138. Copy List with Random Pointer """

import pytest
from leetcode.problems.V0100.T0138_copy_list_with_random_pointer import Node, Solution


@pytest.mark.T0138
def test_copy_list_with_random_pointer_01():

    n1 = Node(1)
    n2 = Node(10, next=n1)
    n3 = Node(11, next=n2)
    n4 = Node(13, next=n3)
    expected = Node(7, next=n4)

    n1.random = expected
    n2.random = n3
    n3.random = n1
    n4.random = expected

    result = Solution().copyRandomList(expected)
    while result and expected:

        assert result.val == expected.val

        if all([result.random, expected.random]):
            assert result.random.val == expected.random.val

        result = result.next
        expected = expected.next

    assert result is None and expected is None


@pytest.mark.T0138
def test_copy_list_with_random_pointer_02():

    n1 = Node(1)
    expected = Node(2, next=n1)

    n1.random = n1
    expected.random = n1

    result = Solution().copyRandomList(expected)
    while result and expected:

        assert result.val == expected.val

        if all([result.random, expected.random]):
            assert result.random.val == expected.random.val

        result = result.next
        expected = expected.next

    assert result is None and expected is None


@pytest.mark.T0138
def test_copy_list_with_random_pointer_03():

    n1 = Node(3)
    n2 = Node(3, next=n1)
    expected = Node(3, next=n1)

    n2.random = n1

    result = Solution().copyRandomList(expected)
    while result and expected:

        assert result.val == expected.val

        if all([result.random, expected.random]):
            assert result.random.val == expected.random.val

        result = result.next
        expected = expected.next

    assert result is None and expected is None
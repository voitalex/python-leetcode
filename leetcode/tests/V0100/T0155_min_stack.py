""" 0155. Min Stack """

import pytest
from leetcode.problems.V0100.T0155_min_stack import MinStack


@pytest.mark.T0155
def test_min_stack():

    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    res = stack.getMin()
    assert res == -3

    stack.pop()

    res = stack.top()
    assert res == 0

    res = stack.getMin()
    assert res == -2

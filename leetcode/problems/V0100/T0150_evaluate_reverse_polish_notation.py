""" 0150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
  * The valid operators are '+', '-', '*', and '/'.
  * Each operand may be an integer or another expression.
  * The division between two integers always truncates toward zero.
  * There will not be any division by zero.
  * The input represents a valid arithmetic expression in a reverse polish notation.
  * The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
    Input: tokens = ["2","1","+","3","*"]
    Output: 9
    Explanation: ((2 + 1) * 3) = 9

Example 2:
    Input: tokens = ["4","13","5","/","+"]
    Output: 6
    Explanation: (4 + (13 / 5)) = 6

Example 3:
    Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    Output: 22
    Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    = ((10 * (6 / (12 * -11))) + 17) + 5
    = ((10 * (6 / -132)) + 17) + 5
    = ((10 * 0) + 17) + 5
    = (0 + 17) + 5
    = 17 + 5
    = 22

Constraints:
  * 1 <= tokens.length <= 10^4
  * tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

from collections import deque
from typing import Dict, Callable, List


class Solution:
    """ Evaluate Reverse Polish Notation """

    OPERATORS: Dict[str, Callable[[int, int], int]] = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        """ Решение задачи """

        stack = deque()
        for token in tokens:

            if token in self.OPERATORS:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.OPERATORS[token](x, y))
            else:
                stack.append(int(token))

        return stack.pop()

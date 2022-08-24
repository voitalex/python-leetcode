""" 0020. Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
  * Open brackets must be closed by the same type of brackets.
  * Open brackets must be closed in the correct order.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([)]"
    Output: false

Example 5:
    Input: s = "{[]}"
    Output: true

Constraints:
  * 1 <= s.length <= 10^4
  * s consists of parentheses only '()[]{}'.
"""

from enum import Enum, unique
from typing import Generic, List, Optional, TypeVar


StackElem = TypeVar('StackElem')


class Stack(Generic[StackElem]):
    """ Реализация стека """

    def __init__(self) -> None:
        self._container: List[StackElem] = []

    def empty(self) -> bool:
        """ Возвращает True если стек не содержит элементов """
        return len(self._container) == 0

    def pop(self) -> None:
        """ Исключает верхний элемент из стека """
        if not self.empty():
            self._container.pop()

    def top(self) -> Optional[StackElem]:
        """ Возвращает элемент на вершине стека """
        if self.empty():
            return None
        return self._container[-1]

    def push(self, item: StackElem) -> None:
        """ Положить новый элемент в стек """
        self._container.append(item)


@unique
class Operation(Enum):
    """ Результат обработки отдельной скобки """
    collapse = 'collapse'
    error = 'error'
    push = 'push'


class Solution:
    """ Valid Parentheses """

    opened_brackets = ('(', '{', '[')
    closed_brackets = (')', '}', ']')

    def process_bracket(self, current: str, last: Optional[str]):
        """ Логика обработки отдельной скобки """

        bracket_pairs = set(zip(self.opened_brackets, self.closed_brackets))

        if last is None or current in set(self.opened_brackets):
            return Operation.push

        if (last, current) in bracket_pairs:
            return Operation.collapse

        return Operation.error

    def isValid(self, brackets: str) -> bool:
        """ Решение задачи """

        stack: Stack[str] = Stack()
        for curr_bracket in brackets:

            last_bracket = stack.top()
            result = self.process_bracket(curr_bracket, last_bracket)
            if result == Operation.push:
                stack.push(curr_bracket)
            elif result == Operation.collapse:
                stack.pop()
            elif result == Operation.error:
                return False

        if not stack.empty():
            return False

        return True

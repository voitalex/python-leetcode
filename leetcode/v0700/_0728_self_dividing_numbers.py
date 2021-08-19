""" 0728. Self Dividing Numbers

Link: https://leetcode.com/problems/self-dividing-numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

Example 1:
    Input: left = 1, right = 22
    Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:
    Input: left = 47, right = 85
    Output: [48,55,66,77]

Constraints:
    1 <= left <= right <= 10^4
"""

from typing import List


class Solution:
    """ Self Dividing Numbers """

    def is_divisible(self, value: int) -> bool:
        """ Возвращает True если число делится на каждую из своих цифр """
        dividers = [int(ch) for ch in str(value)]
        return (0 not in dividers) and (all(value % divider == 0 for divider in dividers))

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """ Решение задачи """
        return [x for x in range(left, right + 1) if self.is_divisible(x)]

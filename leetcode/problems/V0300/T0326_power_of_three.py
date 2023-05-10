""" 0326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
    Input: n = 27
    Output: true

Example 2:
    Input: n = 0
    Output: false

Example 3:
    Input: n = 9
    Output: true

Constraints:
  * -2^31 <= n <= 2^31 - 1
"""


import math


class Solution:
    """ Power of Three """

    def isPowerOfThree(self, n: int) -> bool:
        """ Решение задачи """

        if n <= 0:
            return False

        exp = round(math.log(n, 3))
        return int(pow(3, exp)) == n

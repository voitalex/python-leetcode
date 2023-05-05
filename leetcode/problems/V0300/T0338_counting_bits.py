""" 0338. Counting Bits

Link: https://leetcode.com/problems/counting-bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
    Input: n = 2
    Output: [0,1,1]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10

Example 2:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation:
        0 --> 0
        1 --> 1
        2 --> 10
        3 --> 11
        4 --> 100
        5 --> 101

Constraints:
  * 0 <= n <= 10^5
"""

from typing import List


class Solution:
    """ Counting Bits """

    def countBits(self, n: int) -> List[int]:
        """ Решение задачи """

        result = []
        cache = {0: 0}

        for num in range(n + 1):

            cached = cache[num // 2]
            bits = cached if num % 2 == 0 else cached + 1

            cache[num] = bits
            result.append(bits)

        return result


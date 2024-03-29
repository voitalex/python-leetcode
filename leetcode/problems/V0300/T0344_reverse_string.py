""" 0344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

Constraints:
  * 1 <= s.length <= 10^5
  * s[i] is a printable ascii character.
"""

from typing import List


class Solution:
    """ Reverse String """

    def reverseString(self, s: List[str]) -> List[str]:
        """ Решение задачи """

        return list(reversed(s))

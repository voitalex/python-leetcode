""" 0009. Palindrome Number

Link: https://leetcode.com/problems/palindrome-number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:
    Input: x = 121
    Output: true

Example 2:
    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
                 Therefore it is not a palindrome.

Example 3:
    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
    Input: x = -101
    Output: false

Constraints:
  * -2^31 <= x <= 2^31 - 1
"""


class Solution:
    """ Palindrome Number """

    def isPalindrome(self, x: int) -> bool:
        """ Решение задачи """
        return all(
            map(
                lambda a: a[0] == a[1],
                zip(str(x), reversed(str(x)))
            )
        )

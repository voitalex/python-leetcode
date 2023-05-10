""" 0125. Valid Palindrome

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Constraints:
    1 <= s.length <= 2 * 10^5
    s consists only of printable ASCII characters.
"""


class Solution:
    """ Valid Palindrome """

    def isPalindrome(self, string: str) -> bool:
        """ Решение задачи """

        normalized_string = ''.join([ch for ch in string.lower() if ch.isalnum()])
        return normalized_string == normalized_string[::-1]

""" 0003. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
    Input: s = ""
    Output: 0

Constraints:
  * 0 <= s.length <= 5 * 10^4
  * s consists of English letters, digits, symbols and spaces.
"""

from typing import Dict


class Solution:
    """ Longest Substring Without Repeating Characters """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """ Решение задачи """

        # Текущая максимальная длина последовательности
        max_length = 0

        # Стартовый номер позиции последовательности максимальной длины
        head_index = 0

        # Сопоставление символа и номера позиции в строке, в котором этот символ встретился в последний раз
        char_map: Dict[str, int] = {}

        for index, char in enumerate(s):

            char_map.setdefault(char, -1)

            # Если рассматриваемый символ уже ранее встречался в последовательности,
            # то сдвигаем начало последовательности
            if char_map[char] >= head_index:
                head_index = char_map[char] + 1

            char_map[char] = index
            max_length = max(max_length, index - head_index + 1)

        return max_length

print(Solution().lengthOfLongestSubstring('bbtablud'))
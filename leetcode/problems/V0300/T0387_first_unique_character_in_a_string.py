""" 0387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
    Input: s = "leetcode"
    Output: 0

Example 2:
    Input: s = "loveleetcode"
    Output: 2

Example 3:
    Input: s = "aabb"
    Output: -1

Constraints:
  * 1 <= s.length <= 10^5
  * s consists of only lowercase English letters.
"""

from typing import Dict, Tuple


class Solution:
    """ First Unique Character in a String """

    def firstUniqChar(self, s: str) -> int:
        """ Решение задачи """

        char_map: Dict[str, Tuple[int, int]] = {}
        for index, char in enumerate(s):

            count, min_index = char_map.get(char, (0, index))
            char_map[char] = (count + 1, min(min_index, index))

        min_indexes = [min_index for count, min_index in char_map.values() if count == 1]

        return min(min_indexes) if min_indexes else -1

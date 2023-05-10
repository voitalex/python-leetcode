""" 0500. Keyboards Row

Given an array of strings words, return the words that can be typed using letters of the alphabet on
only one row of American keyboard like the image below.

In the American keyboard:
    the first row consists of the characters "qwertyuiop",
    the second row consists of the characters "asdfghjkl",
    the third row consists of the characters "zxcvbnm".

Example 1:
    Input: words = ["Hello","Alaska","Dad","Peace"]
    Output: ["Alaska","Dad"]

Example 2:
    Input: words = ["omk"]
    Output: []

Example 3:
    Input: words = ["adsdf","sfd"]
    Output: ["adsdf","sfd"]

Constraints:
    1 <= words.length <= 20
    1 <= words[i].length <= 100
    words[i] consists of English letters (both lowercase and uppercase).
"""

from typing import List


class Solution:
    """ Keyboards Row """

    def findWords(self, words: List[str]) -> List[str]:
        """ Решение задачи """

        keyboard_rows = [set(x) for x in ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']]

        return [
            word
            for word in words
            if any(set(word.lower()).issubset(row) for row in keyboard_rows)
        ]

""" 0383. Ransome Note

Link: https://leetcode.com/problems/ransom-note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using
the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false

Example 3:
    Input: ransomNote = "aa", magazine = "aab"
    Output: true

Constraints:
  * 1 <= ransomNote.length, magazine.length <= 105
  * ransomNote and magazine consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    """ Ransom Note """

    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        """ Решение задачи """

        ransom_notes_letters, magazine_letters = Counter(ransom_note), Counter(magazine)

        return all(
            key in magazine_letters and value <= magazine_letters[key]
            for key, value in ransom_notes_letters.items()
        )

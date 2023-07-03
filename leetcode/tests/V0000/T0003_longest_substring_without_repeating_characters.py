""" 0003. Longest Substring Without Repeating Characters """

import pytest
from leetcode.problems.V0000.T0003_longest_substring_without_repeating_characters import Solution


@pytest.mark.T0003
@pytest.mark.parametrize(
    'value, expected',
    [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        ('bbtablud', 6),
    ]
)
def test_two_sums(value, expected):
    assert Solution().lengthOfLongestSubstring(value) == expected

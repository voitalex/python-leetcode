""" 0557. Reverse Words in a String III """

import pytest
from leetcode.problems.V0500.T0557_reverse_words_in_a_string_iii import Solution


@pytest.mark.T0557
@pytest.mark.parametrize(
    'value, expected',
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
    ]
)
def test_sort_array_by_parity(value, expected):
    assert Solution().reverseWords(value) == expected

""" 0151. Reverse Words in a String """


import pytest
from leetcode.v0100._0151_reverse_words_in_a_string import Solution


@pytest.mark.t0151
@pytest.mark.parametrize(
    'value, expected',
    [
        ('the sky is blue', 'blue is sky the'),
        ('  hello world  ', 'world hello'),
        ('a good   example', 'example good a'),
        ('  Bob    Loves  Alice  ', 'Alice Loves Bob'),
        ('Alice does not even like bob', 'bob like even not does Alice'),
    ]
)
def test_reverse_words_in_a_string(value, expected):
    assert Solution().reverseWords(value) == expected

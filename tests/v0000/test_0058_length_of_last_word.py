""" 0058. Length of Last Word """


import pytest
from leetcode.v0000._0058_length_of_last_word import Solution


@pytest.mark.t0058
@pytest.mark.parametrize(
    'value, expected',
    [
        ('Hello World', 5),
        ('   fly me   to   the moon  ', 4),
        ('luffy is still joyboy', 6),
    ]
)
def test_length_of_last_word(value, expected):
    assert Solution().lengthOfLastWord(value) == expected

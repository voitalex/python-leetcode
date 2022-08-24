""" 0058. Length of Last Word """


import pytest
from leetcode.problems.V0000.T0058_length_of_last_word import Solution


@pytest.mark.T0058
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

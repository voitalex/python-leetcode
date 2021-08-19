""" 0804. Unique Morse Code Words """

import pytest
from leetcode.v0800._0804_unique_morse_code_words import Solution


@pytest.mark.t0804
@pytest.mark.parametrize(
    'value, expected',
    [
        (['gin', 'zen', 'gig', 'msg'], 2),
        (['a'], 1),
    ]
)
def test_unique_morse_code_words(value, expected):
    assert Solution().uniqueMorseRepresentations(value) == expected

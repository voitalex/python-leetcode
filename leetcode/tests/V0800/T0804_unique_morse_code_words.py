""" 0804. Unique Morse Code Words """

import pytest
from leetcode.problems.V0800.T0804_unique_morse_code_words import Solution


@pytest.mark.T0804
@pytest.mark.parametrize(
    'value, expected',
    [
        (['gin', 'zen', 'gig', 'msg'], 2),
        (['a'], 1),
    ]
)
def test_unique_morse_code_words(value, expected):
    assert Solution().uniqueMorseRepresentations(value) == expected

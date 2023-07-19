""" 0374. Guess Number Higher or Lower """

import pytest
from leetcode.problems.V0300.T0374_guess_number_higher_or_lower import Solution


@pytest.mark.T0374
@pytest.mark.parametrize(
    'n, pick, expected',
    [
        (10, 6, 6),
        (1, 1, 1),
        (2, 1, 1)
    ]
)
def test_guess_number_higher_or_lower(n, pick, expected):

    def guesser(value):
        if value == pick:
            return 0
        elif value > pick:
            return -1
        else:
            return 1

    assert Solution().guessNumber(n, guess=guesser) == expected

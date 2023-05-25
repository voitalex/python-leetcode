""" 0509. Fibonacci Number """

import pytest
from leetcode.problems.V0500.T0509_fibonacci_number import Solution


@pytest.mark.T0509
@pytest.mark.parametrize(
    'value, expected',
    [
        (2, 1),
        (3, 2),
        (4, 3),
    ]
)
def test_reverse_words_in_a_string(value, expected):
    assert Solution().fib(value) == expected

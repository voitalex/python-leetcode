""" 0150. Evaluate Reverse Polish Notation """

import pytest
from leetcode.problems.V0100.T0150_evaluate_reverse_polish_notation import Solution


@pytest.mark.T0150
@pytest.mark.parametrize(
    'value, expected',
    [
        (['2', '1', '+', '3', '*'], 9),
        (['4', '13', '5', '/', '+'], 6),
        (['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'], 22)
    ]
)
def test_evaluate_reverse_polish_notation(value, expected):
    assert Solution().evalRPN(value) == expected

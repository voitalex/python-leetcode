""" 0020. Valid Parentheses """

import pytest
from leetcode.problems.V0000.T0020_valid_parentheses import Solution


@pytest.mark.T0020
@pytest.mark.parametrize(
    'value, expected',
    [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True),
    ]
)
def test_valid_parentheses(value, expected):
    assert Solution().isValid(value) == expected

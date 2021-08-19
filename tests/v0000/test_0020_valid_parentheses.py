""" 0020. Valid Parentheses """

import pytest
from leetcode.v0000._0020_valid_parentheses import Solution


@pytest.mark.t0020
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


def t1():

    print(Solution().isValid('{[]}'))

t1()
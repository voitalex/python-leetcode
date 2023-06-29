""" 0008. String to Integer """

import pytest
from leetcode.problems.V0000.T0008_string_to_integer import Solution


@pytest.mark.T0008
@pytest.mark.parametrize(
    'value, expected',
    [
        ('42', 42),
        ('-42', -42),
        ('4193 with words', 4193),
        ('words and 987', 0),
        ('-91283472332', -2147483648),
        ('.1', 0),
        ('+-12', 0),
        ('', 0),
        ('2147483648', 2147483647),
    ]
)
def test_string_to_integer(value, expected):
    assert Solution().myAtoi(value) == expected



def t1():
    print(Solution().myAtoi('   -42'))

t1()
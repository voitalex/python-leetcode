""" 0344. Reverse String """

import pytest
from leetcode.problems.V0300.T0344_reverse_string import Solution


@pytest.mark.T0344
@pytest.mark.parametrize(
    'value, expected',
    [
        (['h', 'e', 'l', 'l', 'o'], ['o', 'l', 'l', 'e', 'h']),
        (['H', 'a', 'n', 'n', 'a', 'h'], ['h', 'a', 'n', 'n', 'a', 'H']),
    ]
)
def test_reverse_string(value, expected):
    assert Solution().reverseString(value) == expected

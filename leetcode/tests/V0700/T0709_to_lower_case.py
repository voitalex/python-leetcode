""" 0709. To Lower Case """


import pytest
from leetcode.problems.V0700.T0709_to_lower_case import Solution


@pytest.mark.T0709
@pytest.mark.parametrize(
    'value, expected',
    [
        ('Hello', 'hello'),
        ('here', 'here'),
        ('LOVELY', 'lovely'),
    ]
)
def test_to_lower_case(value, expected):
    assert Solution().toLowerCase(value) == expected

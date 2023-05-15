""" 0067. Add Binary """

import pytest
from leetcode.problems.V0000.T0067_add_binary import Solution


@pytest.mark.T0067
@pytest.mark.parametrize(
    'first, second, expected',
    [
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
    ]
)
def test_add_binary(first, second, expected):
    assert Solution().addBinary(first, second) == expected

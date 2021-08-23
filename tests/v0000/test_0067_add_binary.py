""" 0067. Add Binary """

import pytest
from leetcode.v0000._0067_add_binary import Solution


@pytest.mark.t0067
@pytest.mark.parametrize(
    'first, second, expected',
    [
        ('11', '1', '100'),
        ('1010', '1011', '10101'),
    ]
)
def test_plus_one(first, second, expected):
    assert Solution().addBinary(first, second) == expected

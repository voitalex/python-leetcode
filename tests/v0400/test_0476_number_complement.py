""" 0476. Number Complement """

import pytest
from leetcode.v0400._0476_number_complement import Solution


@pytest.mark.t0476
@pytest.mark.parametrize(
    'value, expected',
    [
        (5, 2),
        (1, 0),
    ]
)
def test_number_complement(value, expected):
    assert Solution().findComplement(value) == expected

""" 0476. Number Complement """

import pytest
from leetcode.problems.V0400.T0476_number_complement import Solution


@pytest.mark.T0476
@pytest.mark.parametrize(
    'value, expected',
    [
        (5, 2),
        (1, 0),
    ]
)
def test_number_complement(value, expected):
    assert Solution().findComplement(value) == expected

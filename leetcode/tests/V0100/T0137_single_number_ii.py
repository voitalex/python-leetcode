""" 0137. Single Number II """

import pytest
from leetcode.problems.V0100.T0137_single_number_ii import Solution


@pytest.mark.T0137
@pytest.mark.parametrize(
    'value, expected',
    [
        ([2,2,3,2], 3),
        ([0,1,0,1,0,1,99], 99),
        ([-2,-2,1,1,4,1,4,4,-4,-2], -4),
    ]
)
def test_single_number_ii(value, expected):
    assert Solution().singleNumber(value) == expected

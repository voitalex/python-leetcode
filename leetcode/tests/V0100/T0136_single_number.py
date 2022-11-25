""" 0136. Single Number """

import pytest
from leetcode.problems.V0100.T0136_single_number import Solution


@pytest.mark.T0136
@pytest.mark.parametrize(
    'value, expected',
    [
        ([2, 2, 1], 1),
        ([4,1,2,1,2], 4),
        ([1], 1),
    ]
)
def test_solution(value, expected):
    assert Solution().singleNumber(value) == expected

""" 0338. Counting Bits """

import pytest
from leetcode.problems.V0300.T0338_counting_bits import Solution


@pytest.mark.T0338
@pytest.mark.parametrize(
    'n, expected',
    [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ]
)
def test_counting_bits(n, expected):
    assert Solution().countBits(n) == expected
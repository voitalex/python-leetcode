""" 0190. Reverse Bits """

import pytest
from leetcode.problems.V0100.T0190_reverse_bits import Solution


@pytest.mark.T0190
@pytest.mark.parametrize(
    'n, result',
    [
        (43261596, 964176192),
        (4294967293, 3221225471),
    ]
)
def test_reverse_bits(n, result):
    assert Solution().reverseBits(n) == result

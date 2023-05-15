""" 0191. Number of 1 Bits """

import pytest
from leetcode.problems.V0100.T0191_number_of_1_bits import Solution


@pytest.mark.T0191
@pytest.mark.parametrize(
    'n, result',
    [
        (11, 3),
        (128, 1),
        (4294967293, 31),
    ]
)
def test_number_of_1_bits(n, result):
    assert Solution().hammingWeight(n) == result

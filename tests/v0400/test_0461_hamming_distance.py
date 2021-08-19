""" 0461. Hamming Distance """

import pytest
from leetcode.v0400._0461_hamming_distance import Solution


@pytest.mark.t0461
@pytest.mark.parametrize(
    'first, second, expected',
    [
        (1, 4, 2),
        (3, 1, 1),
    ]
)
def test_hamming_distance(first, second, expected):
    assert Solution().hammingDistance(first, second) == expected

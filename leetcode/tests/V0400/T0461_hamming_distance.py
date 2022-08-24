""" 0461. Hamming Distance """

import pytest
from leetcode.problems.V0400.T0461_hamming_distance import Solution


@pytest.mark.T0461
@pytest.mark.parametrize(
    'first, second, expected',
    [
        (1, 4, 2),
        (3, 1, 1),
    ]
)
def test_hamming_distance(first, second, expected):
    assert Solution().hammingDistance(first, second) == expected

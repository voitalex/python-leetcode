""" 1512. Number of Good Pairs """

import pytest
from leetcode.problems.V1500.T1512_number_of_good_pairs import Solution


@pytest.mark.T1512
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 2, 3, 1, 1, 3], 4),
        ([1, 1, 1, 1], 6),
        ([1, 2, 3], 0),
    ]
)
def test_number_of_good_pairs(value, expected):
    assert Solution().numIdenticalPairs(value) == expected

""" 0771. Jewels and Stones """

import pytest
from leetcode.problems.V0700.T0771_jewels_and_stones import Solution


@pytest.mark.T0771
@pytest.mark.parametrize(
    'jewels, stones, expected',
    [
        ('aA', 'aAAbbbb', 3),
        ('z', 'ZZ', False),
    ]
)
def test_jewels_and_stones(jewels, stones, expected):
    assert Solution().numJewelsInStones(jewels, stones) == expected

""" 0066. Plus One """

import pytest
from leetcode.v0000._0066_plus_one import Solution


@pytest.mark.t0066
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([0], [1]),
    ]
)
def test_plus_one(value, expected):
    assert Solution().plusOne(value) == expected

""" 0268. Missing Number """

import pytest
from leetcode.problems.V0200.T0268_missing_number import Solution


@pytest.mark.T0268
@pytest.mark.parametrize(
    'value, expected',
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),

    ]
)
def test_missing_number(value, expected):
    assert Solution().missingNumber(value) == expected

""" 1207. Unique Number of Occurrences """

import pytest
from leetcode.v1200._1207_unique_number_of_ocurrences import Solution


@pytest.mark.t1207
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10 , 0], True),
    ]
)
def test_unique_occurrences(value, expected):
    assert Solution().uniqueOccurrences(value) == expected

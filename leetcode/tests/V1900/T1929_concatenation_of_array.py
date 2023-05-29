""" 1929. Concatenation of Array """

import pytest
from leetcode.problems.V1900.T1929_concatenation_of_array import Solution


@pytest.mark.T1929
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
    ]
)
def test_unique_number_of_occurrences(value, expected):
    assert Solution().getConcatenation(value) == expected

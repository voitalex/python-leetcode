""" 0028. Find the Index of the First Occurrence in a String """

import pytest
from leetcode.problems.V0000.T0028_find_the_index_of_the_first_occurrence_in_a_string import Solution


@pytest.mark.T0028
@pytest.mark.parametrize(
    'needle, haystack, expected',
    [
        ('hello', 'll', 2),
        ('aaaaa', 'bba',  -1),
        ('', '', 0),
    ]
)
def test_valid_parentheses(needle, haystack, expected):
    assert Solution().strStr(needle, haystack) == expected

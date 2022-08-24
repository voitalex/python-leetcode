""" 0028. Implement strStr() """

import pytest
from leetcode.problems.V0000.T0028_implement_strstr import Solution


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

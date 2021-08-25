""" 0028. Implement strStr() """

import pytest
from leetcode.v0000._0028_implement_strstr import Solution


@pytest.mark.t0028
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

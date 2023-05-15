""" 0014. Longest Common Prefix """

import pytest
from leetcode.problems.V0000.T0014_longest_common_prefix import Solution


@pytest.mark.T0014
@pytest.mark.parametrize(
    'value, expected',
    [
        (['flower', 'flow', 'flight'], 'fl'),
        (['dog', 'racecar', 'car'], ''),
    ]
)
def test_longest_common_prefix(value, expected):
    assert Solution().longestCommonPrefix(value) == expected

""" 0389. Find the difference """

import pytest
from leetcode.problems.V0300.T0389_find_the_difference import Solution


@pytest.mark.T0389
@pytest.mark.parametrize(
    's, t, expected',
    [
        ('abcd', 'abcde', 'e'),
        ('', 'y', 'y'),
    ]
)
def test_find_the_difference(s, t, expected):
    assert Solution().findTheDifference(s, t) == expected

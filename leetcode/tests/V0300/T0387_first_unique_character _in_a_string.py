""" 0387. First Unique Character in a String """

import pytest
from leetcode.problems.V0300.T0387_first_unique_character_in_a_string import Solution


@pytest.mark.T0387
@pytest.mark.parametrize(
    'value, expected',
    [
        ('leetcode', 0),
        ('loveleetcode', 2),
        ('aabb', -1),
    ]
)
def test_first_unique_character_in_a_string(value, expected):
    assert Solution().firstUniqChar(value) == expected

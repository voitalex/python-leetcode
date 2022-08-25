""" 0383. Ransom Note """

import pytest
from leetcode.problems.V0300.T0383_ransom_note import Solution


@pytest.mark.T0383
@pytest.mark.parametrize(
    'ransom_note, magazine, expected',
    [
        ('a', 'b', False),
        ('aa', 'ab', False),
        ('aa', 'aab', True),
    ]
)
def test_power_of_three(ransom_note, magazine, expected):
    assert Solution().canConstruct(ransom_note, magazine) == expected

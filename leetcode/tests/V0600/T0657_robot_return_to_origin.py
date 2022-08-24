""" 0657. Robot Return to Origin """

import pytest
from leetcode.problems.V0600.T0657_robot_return_to_origin import Solution


@pytest.mark.T0657
@pytest.mark.parametrize(
    'value, expected',
    [
        ('UD', True),
        ('LL', False),
        ('RRDD', False),
        ('LDRRLRUULR', False),
    ]
)
def test_robot_return_to_origin(value, expected):
    assert Solution().judgeCircle(value) == expected

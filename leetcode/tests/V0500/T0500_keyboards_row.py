""" 0500. Keyboards Row """

import pytest
from leetcode.problems.V0500.T0500_keyboards_row import Solution


@pytest.mark.T0500
@pytest.mark.parametrize(
    'value, expected',
    [
        (['Hello', 'Alaska', 'Dad', 'Peace'], ['Alaska', 'Dad']),
        (['omk'], []),
    ]
)
def test_keyboards_row(value, expected):
    assert Solution().findWords(value) == expected


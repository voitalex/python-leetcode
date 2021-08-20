""" 0500. Keyboards Row """

import pytest
from leetcode.v0500._0500_keyboards_row import Solution


@pytest.mark.t0500
@pytest.mark.parametrize(
    'value, expected',
    [
        (['Hello', 'Alaska', 'Dad', 'Peace'], ['Alaska', 'Dad']),
        (['omk'], []),
    ]
)
def test_keyboards_row(value, expected):
    assert Solution().findWords(value) == expected


""" 0728. Self Dividing Numbers """


import pytest
from leetcode.problems.V0700.T0728_self_dividing_numbers import Solution


@pytest.mark.T0728
@pytest.mark.parametrize(
    'left, right, expected',
    [
        (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
        (47, 85, [48, 55, 66, 77]),
    ]
)
def test_self_dividing_numbers(left, right, expected):
    assert Solution().selfDividingNumbers(left, right) == expected

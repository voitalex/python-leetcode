""" 0035. Search Insert Position """


import pytest
from leetcode.v0000._0035_search_insert_position import Solution


@pytest.mark.t0035
@pytest.mark.parametrize(
    'numbers, target, expected',
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1], 0, 0),
    ]
)
def test_solution(numbers, target, expected):
    assert Solution().searchInsert(numbers, target) == expected



def t1():
    print(Solution().searchInsert([1, 3, 5, 6], 2))

t1()
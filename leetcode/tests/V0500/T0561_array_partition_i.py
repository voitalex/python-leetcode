""" 0561. Array Partition I """

import pytest
from leetcode.problems.V0500.T0561_array_partition_i import Solution


@pytest.mark.T0561
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 4, 3, 2], 4),
        ([6, 2, 6, 5, 1, 2], 9)
    ]
)
def test_array_partition(value, expected):
    assert Solution().arrayPairSum(value) == expected

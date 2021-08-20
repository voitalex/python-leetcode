""" 0561. Array Partition I """

import pytest
from leetcode.v0500._0561_array_partition_i import Solution


@pytest.mark.t0561
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1, 4, 3, 2], 4),
        ([6, 2, 6, 5, 1, 2], 9)
    ]
)
def test_array_partition(value, expected):
    assert Solution().arrayPairSum(value) == expected

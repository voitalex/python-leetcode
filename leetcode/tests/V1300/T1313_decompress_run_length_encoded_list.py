""" 1313. Decompress Run-Length Encoded List
 """

import pytest
from leetcode.problems.V1300.T1313_decompress_run_length_encoded_list import Solution


@pytest.mark.T1313
@pytest.mark.parametrize(
    'value, expected',
    [
        ([1,2,3,4], [2,4,4,4]),
        ([1,1,2,3], [1,3,3]),
    ]
)
def test_decompress_run_length_encoded_list(value, expected):
    assert Solution().decompressRLElist(value) == expected

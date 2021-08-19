""" 1108. Defanging an IP Address """

import pytest
from leetcode.v1100._1108_defanging_an_ip_address import Solution


@pytest.mark.t1108
@pytest.mark.parametrize(
    'value, expected',
    [
        ('1.1.1.1', '1[.]1[.]1[.]1'),
        ('255.100.50.0', '255[.]100[.]50[.]0'),
    ]
)
def test_two_sums(value, expected):
    assert Solution().defangIPaddr(value) == expected

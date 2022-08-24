""" 1108. Defanging an IP Address """

import pytest
from leetcode.problems.V1100.T1108_defanging_an_ip_address import Solution


@pytest.mark.T1108
@pytest.mark.parametrize(
    'value, expected',
    [
        ('1.1.1.1', '1[.]1[.]1[.]1'),
        ('255.100.50.0', '255[.]100[.]50[.]0'),
    ]
)
def test_defanging_an_ip_address(value, expected):
    assert Solution().defangIPaddr(value) == expected

""" 0002. Add Two Numbers """

import pytest
from add_two_numbers import ListNode, Solution


@pytest.mark.t0002
@pytest.mark.parametrize(
    'first, second, expected',
    [
        (ListNode(2, ListNode(4, ListNode(3))),
         ListNode(5, ListNode(6, ListNode(4))),
         ListNode(7, ListNode(0, ListNode(8)))),
        (ListNode(0), ListNode(0), ListNode(0)),
        (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
         ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
         ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))),
    ]
)
def test_add_two_sums(first, second, expected):

    def nums_from_list(lst: ListNode):
        digits = []
        while lst:
            digits.append(lst.value)
            lst = lst.next
        return digits

    result_digits = nums_from_list(Solution().addTwoNumbers(first, second))
    expected_digits = nums_from_list(expected)

    assert result_digits == expected_digits

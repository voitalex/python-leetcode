""" 0461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

Example 1:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    The above arrows point to positions where the corresponding bits are different.

Example 2:
    Input: x = 3, y = 1
    Output: 1

Constraints:
    0 <= x, y <= 2^31 - 1
"""


class Solution:
    """ Hamming Distance """

    def hammingDistance(self, x: int, y: int) -> int:
        """ Решение задачи """

        str_x, str_y = f'{x:0>100b}', f'{y:0>100b}'
        return sum(1 for first, second in zip(str_x, str_y) if first != second)

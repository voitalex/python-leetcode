""" 0069. Sqrt(x)

Link: https://leetcode.com/problems/sqrtx

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result
is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:
    Input: x = 4
    Output: 2

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

Constraints:
  * 0 <= x <= 2^31 - 1
"""


class Solution:
    """ Sqrt(x) """

    def mySqrt(self, x: int) -> int:
        """ Решение задачи """

        if x <= 0:
            return 0

        square_root: int = 1
        decreased: bool = False
        while True:
            guess = (square_root + int(x / square_root)) // 2

            # Текущий вариант ответа может начать "скакать" возле искомого ответа. Поэтому мы добавляем условие,
            # что если текущий вариант ответа на предыдущем шаге уменьшился, а на текущем шаге пытается увеличиться,
            # то алгоритм надо остановить.
            if square_root == guess or (guess > square_root and decreased):
                break

            decreased = guess < square_root
            square_root = guess

        return square_root

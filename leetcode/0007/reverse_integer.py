""" 0007. Reverse Integer """

class Solution:
    """ Reverse Integer """

    def reverse(self, x: int) -> int:
        """ Решение задачи """

        sign = 1 if x >= 0 else -1
        result = sign * int(str(abs(x))[::-1])

        if -1 * (2**31) <= result <= (2**31) - 1:
            return result

        return 0

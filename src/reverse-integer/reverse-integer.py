# // https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x_abs = abs(x)
        result = 0

        while x_abs:
            last_digit = x_abs % 10
            x_abs //= 10
            result = result * 10 + last_digit

        if result > 2 ** 31:
            result = 0

        return -result if negative else result
        
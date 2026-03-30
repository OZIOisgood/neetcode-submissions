class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign
        res = 0
        while x:
            digit = x % 10
            res = res * 10 + digit
            x //= 10

        res *= sign
        return res if -(1 << 31) < res < (1 << 31) - 1 else 0
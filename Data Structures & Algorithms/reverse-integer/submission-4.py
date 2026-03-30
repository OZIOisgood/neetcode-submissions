class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x if sign == 1 else -x

        res = 0
        while x:
            res = res * 10 + (x % 10)
            x //= 10

        res *= sign
        return 0 if res < -(1 << 31) or res > (1 << 31) - 1 else res

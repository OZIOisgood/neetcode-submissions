class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            digit = (n >> i) & 1
            res = (res << 1) + digit
        return res
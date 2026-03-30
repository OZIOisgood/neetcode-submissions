class Solution:
    def reverseBits(self, n: int, res = 0) -> int:
        for i in range(32): res = (res << 1) |  (n >> i) & 1
        return res
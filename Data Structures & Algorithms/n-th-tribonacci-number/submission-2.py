class Solution:
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]

        if n < 3:
            return t[n]

        for i in range(3, n + 1):
            next_value = sum(t)
            t[0] = t[1]
            t[1] = t[2]
            t[2] = next_value

        return t[2]
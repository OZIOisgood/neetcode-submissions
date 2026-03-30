class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        def helper(x, n):
            sub = n // 2
            res = 1 if sub == 0 else helper(x * x, sub)

            isOdd = n % 2
            if isOdd:
                return x * res
            else:
                return res

        if n >= 0:
            return helper(x, n)
        else:
            return 1 / helper(x, abs(n))
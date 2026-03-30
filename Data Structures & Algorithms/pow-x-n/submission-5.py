class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        def helper(x, n):
            if n == 0: return 1
            if n == 1: return x
            
            res = helper(x, n // 2)

            isOdd = n % 2
            if isOdd:
                return res * res * x
            else:
                return res * res

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
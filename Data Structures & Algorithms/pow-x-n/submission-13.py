class Solution:
    def myPow(self, x: float, n: int) -> float:
        def dfs(x, n):
            if n == 0: return 1
            if n == 1: return x
            if x == 0: return 0
            
            isOdd = n % 2 != 0
            res = dfs(x, n // 2)
            
            if isOdd == True:
                return res * res * x
            else:
                return res * res
            
        if n < 0:
            return 1 / dfs(x, -n)
        else:
            return dfs(x, n)
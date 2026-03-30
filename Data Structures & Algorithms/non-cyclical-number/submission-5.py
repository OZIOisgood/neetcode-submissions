class Solution:
    def isHappy(self, n: int) -> bool:
        visit = {n}
        while n != 1:
            n = self.getCal(n)
            if n in visit: return False
            visit.add(n)
        return True

    def getCal(self, n: int) -> int:
        x = 0
        while n:
            x += (n % 10) ** 2
            n //= 10
        return x
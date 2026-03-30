class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n != 1:
            if n in visit: return False
            visit.add(n)
            n = self.getCal(n)

        return True

    def getCal(self, n: int) -> int:
        x = 0
        while n:
            x += (n % 10) ** 2
            n //= 10
        return x
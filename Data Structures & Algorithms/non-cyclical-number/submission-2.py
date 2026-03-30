class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)

        while fast != 1 and slow != fast:
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)
            
        return fast == 1

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        
        return output
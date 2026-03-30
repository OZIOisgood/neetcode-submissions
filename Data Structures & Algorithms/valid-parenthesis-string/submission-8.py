class Solution:
    def checkValidString(self, s: str) -> bool:
        minVal = maxVal = 0

        for p in s:
            if p == '(':
                minVal += 1
                maxVal += 1
            elif p == ')':
                minVal -= 1
                maxVal -= 1
            elif p == '*':
                minVal -= 1
                maxVal += 1
            
            if maxVal < 0: return False
            if minVal < 0: minVal = 0
        
        return minVal <= 0
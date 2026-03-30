class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits.reverse()
        cur = 0; one = 1
        while one == 1 and cur < n:
            if digits[cur] == 9: digits[cur] = 0
            else:
                digits[cur] += 1
                one = 0
            cur += 1
        if one == 1: digits.append(1)
        digits.reverse()
        return digits
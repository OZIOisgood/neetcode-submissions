class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True
        
        for start in range(len(s)):
            for end in range(start, len(s)):
                if isPali(start, end): res += 1
        
        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]; n = len(s)
        
        for i in range(n):
            h1 = self.help(s, i, i)
            h2 = self.help(s, i, i + 1)
            if len(h1) > len(res): res = h1
            if len(h2) > len(res): res = h2
        
        return res

    def help(self, s: str, l: int, r: int) -> str:
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]
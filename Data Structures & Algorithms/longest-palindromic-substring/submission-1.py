class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""; resLen = 0
        for i in range(len(s)):
            #odd
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    res = s[l:r+1]
                    resLen = length
                l -= 1
                r += 1

            # even
            l = i; r = i + 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > resLen:
                    res = s[l:r+1]
                    resLen = length
                l -= 1
                r += 1
        
        return res
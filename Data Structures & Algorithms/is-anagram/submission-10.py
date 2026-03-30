class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hS, hT = {}, {}

        for i in range(len(s)):
            sL, tL = s[i], t[i]
            
            hS[sL] = hS.get(sL, 0) + 1
            hT[tL] = hT.get(tL, 0) + 1

        return hS == hT
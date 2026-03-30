class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            sHM, tHM = {}, {}

            for i in range(len(s)):
                sHM[s[i]] = sHM.get(s[i], 0) + 1
                tHM[t[i]] = tHM.get(t[i], 0) + 1
            
            return sHM == tHM
        
        return False
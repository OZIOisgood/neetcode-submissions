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
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s)

        return list(res.values())
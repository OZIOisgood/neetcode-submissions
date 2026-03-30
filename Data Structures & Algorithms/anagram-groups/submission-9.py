class Solution:
    def getWordHashMap(self, s: str) -> List[int]:
        res = [0] * 26

        for c in s:
            res[ord(c) - ord('a')] += 1

        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        print(res)

        for s in strs:
            h = self.getWordHashMap(s)
            res[tuple(h)].append(s)
            print(res)

        return list(res.values())
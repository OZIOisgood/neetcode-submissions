class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = defaultdict(list)
        for s in strs:
            stamp = tuple(sorted(Counter(s).items()))
            ht[stamp].append(s)
        return list(ht.values())
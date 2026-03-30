class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        q = {0: 1}
        for n in nums:
            nxt = defaultdict(int)
            for s, cnt in q.items():
                nxt[s + n] += cnt
                nxt[s - n] += cnt
            q = nxt
        return q[target]
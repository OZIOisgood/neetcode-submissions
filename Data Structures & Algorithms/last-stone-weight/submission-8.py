class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones); b = heapq.heappop_max(stones)
            if a == b: continue
            a -= b
            heapq.heappush_max(stones, a)
        return stones[0] if stones else 0
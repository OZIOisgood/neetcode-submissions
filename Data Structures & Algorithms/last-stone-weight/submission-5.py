class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            y, x = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if x < y: heapq.heappush_max(stones, y - x)
        stones.append(0)
        return stones[0]
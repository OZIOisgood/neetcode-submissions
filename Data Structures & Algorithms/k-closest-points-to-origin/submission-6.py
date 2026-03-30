class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        x1, y1 = 0, 0
        for x2, y2 in points:
            length = (x1 - x2) ** 2 + (y1 - y2) ** 2
            heapq.heappush_max(h, (length, [x2, y2]))

            if len(h) > k:
                heapq.heappop_max(h)
        
        return [point for _, point in h]
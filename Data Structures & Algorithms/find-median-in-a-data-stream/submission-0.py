class MedianFinder:
    def __init__(self):
        self.small, self.large = [], [] # minHeap and maxHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return ((self.small[0] * -1) + self.large[0]) / 2.0
        
        
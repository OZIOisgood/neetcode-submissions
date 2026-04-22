class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (нижняя половина)
        self.large = []  # min-heap (верхняя половина)

    def addNum(self, num: int) -> None:
        # 1. Добавляем в max-heap
        heapq.heappush_max(self.small, num)

        # 2. Самый большой из нижней половины перекидываем в верхнюю
        val = heapq.heappop_max(self.small)
        heapq.heappush(self.large, val)

        # 3. Держим инвариант по размерам: small либо такой же, либо на 1 больше
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush_max(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(self.small[0])
        return (self.small[0] + self.large[0]) / 2

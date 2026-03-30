class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        count = Counter(hand)
        h = list(count.keys()); heapq.heapify(h)
        while h:
            start = v = h[0]
            while v < start + groupSize:
                if v not in count: return False
                count[v] -= 1
                if count[v] == 0:
                    del count[v]
                    heapq.heappop(h)
                v += 1
        return True
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0: return False
        c = Counter(hand)
        
        h = list(c.keys())
        heapq.heapify(h)
        while h:
            first = h[0]
            for i in range (first, first + groupSize):
                if i not in c: return False
                c[i] -= 1
                if c[i] == 0:
                    # if i != h[0]: return False
                    heapq.heappop(h)

        return True
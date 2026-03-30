class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1; r = max(piles)

        res = r
        while l <= r:
            k = l + (r - l) // 2

            cur_h = 0
            for p in piles:
                cur_h += math.ceil(p / k)

            if cur_h <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
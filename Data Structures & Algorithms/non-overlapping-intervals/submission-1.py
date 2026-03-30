class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        res = 0
        prevEnd = None
        for cur in intervals:
            start, end = cur

            if prevEnd == None or prevEnd <= start:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(
                    end,
                    prevEnd
                )

        return res
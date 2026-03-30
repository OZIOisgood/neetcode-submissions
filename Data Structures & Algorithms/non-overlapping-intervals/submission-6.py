class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        _, prev_end = intervals[0]
        
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            
            if prev_end > cur_start:
                res += 1
                prev_end = min(prev_end, cur_end)
            else:
                prev_end = cur_end
        
        return res
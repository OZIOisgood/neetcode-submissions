class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(
            key = lambda pair: pair[0]
        )
        res = []

        for curInterval in intervals:
            if len(res) == 0:
                res.append(curInterval)
            else:
                start, end = curInterval
                lastEnd = res[-1][1]

                if start <= lastEnd:
                    res[-1][1] = max(
                        lastEnd,
                        end
                    )
                else:
                    res.append(curInterval)
        
        return res

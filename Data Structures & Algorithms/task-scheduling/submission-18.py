class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mH = list(Counter(tasks).values())
        heapq.heapify_max(mH)
        time = 0
        q = deque()
        while mH or q:
            time += 1

            if mH:
                cnt = heapq.heappop_max(mH) - 1
                if cnt: q.append([cnt, time + n])
            
            if q and q[0][1] == time: heapq.heappush_max(mH, q.popleft()[0])
        return time
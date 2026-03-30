class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        h = list(Counter(tasks).values())
        heapq.heapify_max(h)
        time = 0
        q = deque()
        while h or q:
            time += 1

            if h:
                cnt = heapq.heappop_max(h) - 1
                if cnt: q.append([cnt, time + n])
            
            if q and q[0][1] == time: heapq.heappush_max(h, q.popleft()[0])
        return time
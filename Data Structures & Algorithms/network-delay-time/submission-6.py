class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        h = [(0, k)]
        visit = set()
        t_max = 0
        while h:
            t1, n1 = heapq.heappop(h)

            if n1 not in visit:
                visit.add(n1)
                t_max = t1
                for n2, t2 in adj[n1]:
                    if n2 not in visit:
                        heapq.heappush(h, (t1 + t2, n2))

        return t_max if len(visit) == n else -1

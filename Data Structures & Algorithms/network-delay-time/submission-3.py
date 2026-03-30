class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        h = [(0, k)]
        visit = set()
        t = 0
        while h:
            w1, n1 = heapq.heappop(h)
            if n1 not in visit:
                visit.add(n1)
                t = w1
                for n2, w2 in adj[n1]:
                    if n2 not in visit:
                        heapq.heappush(h, (w1 + w2, n2))

        return t if len(visit) == n else -1
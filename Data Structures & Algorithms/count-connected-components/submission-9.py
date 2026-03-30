class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visit = [False] * n
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        
        return res
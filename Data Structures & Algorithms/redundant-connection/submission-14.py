class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def hasCycle():
            visited = set()

            def dfs(u, parent):
                visited.add(u)
                for nei in adj[u]:
                    if nei == parent: continue
                    if nei in visited: return True
                    if dfs(nei, u): return True
                return False

            for node in adj:
                if node not in visited:
                    if dfs(node, -1):
                        return True
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if hasCycle():
                return [u, v]

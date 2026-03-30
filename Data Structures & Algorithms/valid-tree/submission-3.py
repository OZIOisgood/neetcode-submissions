class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        adj = defaultdict(list)

        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        
        seen = set()
        def dfs(node, parent):
            if node in seen: return False

            seen.add(node)
            for nei in adj[node]:
                if nei == parent: continue
                if not dfs(nei, node): return False
            
            return True
        
        return dfs(0, -1) and len(seen) == n
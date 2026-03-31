class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        
        visited = set()
        path    = set()
        def dfs(node):
            if node in path: return False
            if node in visited: return True
            path.add(node)
            
            for nei in adj[node]:
                if dfs(nei) == False:
                    return False

            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(0, numCourses):
            if i not in visited:
                if dfs(i) == False:
                    return False
        
        return True
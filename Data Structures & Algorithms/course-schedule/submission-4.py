class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        # 0 = unvisited, 1 = visiting (in current recursion stack), 2 = done
        state = [0] * numCourses

        def dfs(i: int) -> bool:
            if state[i] == 1:   # found a cycle
                return False
            if state[i] == 2:   # already checked, no cycle from here
                return True

            state[i] = 1
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            state[i] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
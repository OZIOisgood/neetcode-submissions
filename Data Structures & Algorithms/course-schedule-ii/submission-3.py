class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj[course] = list of prerequisite courses
        adj = defaultdict(list)
        for course, pre in prerequisites:
            adj[course].append(pre)

        res: List[int] = []
        # 0 = unvisited, 1 = visiting (in current path), 2 = done
        state = [0] * numCourses

        def dfs(i: int) -> bool:
            if state[i] == 1:
                return False  # cycle
            if state[i] == 2:
                return True   # already processed

            state[i] = 1
            for pre in adj[i]:
                if not dfs(pre):
                    return False
            state[i] = 2
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
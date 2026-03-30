class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                not (0 <= r < R) or
                not (0 <= c < C) or
                heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            for dx, dy in DIRS:
                dfs(r + dx, c + dy, visit, heights[r][c])

        for c in range(C):
            dfs(0, c, pac, heights[0][c])
            dfs(R - 1, c, atl, heights[R - 1][c])
        
        for r in range(R):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, C - 1, atl, heights[r][C - 1])

        res = []
        for r in range(R):
            for c in range(C):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
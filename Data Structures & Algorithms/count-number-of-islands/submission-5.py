class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        R, C = len(grid), len(grid[0])
        res = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if not (nr < 0 or nc < 0 or nr >= R or
                        nc >= C or grid[nr][nc] == "0"
                    ):
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1

        return res
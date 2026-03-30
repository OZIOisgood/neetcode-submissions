class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF     = 2147483647
        WALL    = -1
        CHEST   = 0
        M       = len(grid)
        N       = len(grid[0])

        chest_positions = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == CHEST:
                    chest_positions.append((i,j))
        
        steps = 0
        q = deque(chest_positions)
        visit = set(chest_positions)
        while q:
            q_init_size = len(q)

            for _ in range(q_init_size):
                i, j = q.popleft()
                grid[i][j] = steps
                
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + dr, j + dc

                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == INF and ((ni, nj) not in visit):
                        visit.add((ni, nj))
                        q.append((ni, nj))
                        
            steps += 1
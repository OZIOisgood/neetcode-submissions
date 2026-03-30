class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        targets = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    targets.append((i, j))
        
        length = 0
        deq = deque(targets)  
        while deq:
            nextDeq = deque()
            for i, j in deq:
                cur = grid[i][j]
                if (
                    cur == INF or
                    cur == 0
                ):
                    grid[i][j] = length

                    for dr, dc in dirs:
                        ni, nj = i + dr, j + dc
                        if (
                            0 <= ni < ROWS and
                            0 <= nj < COLS and
                            grid[ni][nj] == INF
                        ):
                            nextDeq.append((ni, nj))
            
            deq = nextDeq
            length += 1
            
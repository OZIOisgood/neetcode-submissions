DIRS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        visit = set([(0, 0)]); minH = [[grid[0][0], 0, 0]]  # (time, row, col)
        while minH:
            t, r, c = heapq.heappop(minH)
            if (r, c) == (N - 1, N - 1): return t
            for dr, dc in DIRS:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        total = R * C
        res = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r = 0
        c = 0

        while len(res) < total:
            res.append(matrix[r][c])
            matrix[r][c] = 'X'  # mark visited

            dr, dc = directions[d]
            nr, nc = r + dr, c + dc

            # if next is invalid, turn right
            if (nr < 0 or nr >= R or
                nc < 0 or nc >= C or
                matrix[nr][nc] == 'X'):
                d = (d + 1) % 4
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc

            r, c = nr, nc

        return res

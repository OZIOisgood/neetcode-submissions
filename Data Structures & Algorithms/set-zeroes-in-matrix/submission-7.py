class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix);     COLS = len(matrix[0])
        LEFT = [False] * ROWS;  TOP = [False] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    LEFT[i] = TOP[j] = True

        for i in range(ROWS):
            for j in range(COLS):
                if LEFT[i] or TOP[j]:
                    matrix[i][j] = 0
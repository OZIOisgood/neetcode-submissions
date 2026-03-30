class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix); C = len(matrix[0])
        l = 0; r = R * C - 1

        while l <= r:
            m = l + (r - l) // 2
            row = m // C; col = m % C
            if target > matrix[row][col]: l = m + 1
            elif target < matrix[row][col]: r = m - 1
            else: return True
        
        return False
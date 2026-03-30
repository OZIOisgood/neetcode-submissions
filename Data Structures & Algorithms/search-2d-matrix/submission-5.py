class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix); COLS = len(matrix[0]);
        l = 0; r = (ROWS * COLS) - 1

        while l <= r:
            m_idx = l + (r - l) // 2

            m_ROW = m_idx // COLS
            m_COL = m_idx % COLS
            m = matrix[m_ROW][m_COL]
            
            if m == target:
                return True
            elif m > target:
                r = m_idx - 1
            elif m < target:
                l = m_idx + 1
        
        return False
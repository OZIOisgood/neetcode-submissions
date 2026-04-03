class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(0, 9):
            for c in range(0, 9):
                n = board[r][c]
                nBlockIndex = (r // 3, c // 3)
                if n == ".":
                    continue
                
                if (n in rows[r] or
                    n in cols[c] or
                    n in blocks[nBlockIndex]):
                    return False
                
                cols[c].add(n)
                rows[r].add(n)
                blocks[nBlockIndex].add(n)
        
        return True
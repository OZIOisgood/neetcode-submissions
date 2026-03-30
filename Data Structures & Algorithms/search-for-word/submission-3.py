from typing import List, Set, Tuple

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        path: Set[Tuple[int, int]] = set()

        def dfs(r: int, c: int, i: int) -> bool:
            # All characters matched
            if i == len(word):
                return True

            # Out of bounds or char mismatch or cell already used in current path
            if (
                r < 0 or c < 0 or
                r == R or c == C or
                board[r][c] != word[i] or
                (r, c) in path
            ):
                return False

            # Choose current cell
            path.add((r, c))

            # Explore neighbors
            for dx, dy in dirs:
                if dfs(r + dx, c + dy, i + 1):
                    return True

            # Backtrack
            path.remove((r, c))
            return False

        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True

        return False

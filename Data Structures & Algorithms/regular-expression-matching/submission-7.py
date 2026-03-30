class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if (i, j) in cache: return cache[(i, j)]
            if i >= m and j >= n: return True
            if j >= n: return False

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                cache[(i, j)] = (
                    dfs(i, j + 2) or          # not use *
                    (match and dfs(i + 1, j)) #     use *
                )
                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False
        
        return dfs(0, 0)
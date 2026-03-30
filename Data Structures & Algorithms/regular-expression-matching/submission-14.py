class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n, cache = len(s), len(p), {}
        def put(i, j, value):
            cache[i, j] = value
            return value
        def dfs(i, j):
            if j == n: return i == m
            if (i, j) in cache: return cache[(i, j)]

            match = i < m and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < n and p[j + 1] == "*":
                return put(i, j, dfs(i, j + 2) or (match and dfs(i + 1, j)))
            elif match:
                return put(i, j, dfs(i + 1, j + 1))
            else:
                return put(i, j, False)
        return dfs(0, 0)
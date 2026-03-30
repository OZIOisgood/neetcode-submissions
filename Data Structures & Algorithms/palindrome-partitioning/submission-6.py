class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []; path = []

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def bt(i):
            if i == n:
                res.append(path.copy())
                return

            for j in range(i, n):
                if not isPali(i, j): continue
                path.append(s[i:j + 1])
                bt(j + 1)
                path.pop()

        bt(0)
        return res

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if (l1 + l2) != l3: return False

        dp = {}
        def dfs(i = 0, j = 0):
            k = i + j
            if (i == l1 and
                j == l2 and
                k == l3):
                return True
            if (i > l1 or
                j > l2 or
                k > l3):
                return False

            if (i, j) not in dp:
                res = False
    
                if i < l1 and s1[i] == s3[k]:
                    if dfs(i + 1, j):
                        res = True
    
                if res == False and j < l2 and s2[j] == s3[k]:
                    if dfs(i, j + 1):
                        res = True

                dp[(i, j)] = res
            
            return dp[(i, j)]
        
        return dfs()
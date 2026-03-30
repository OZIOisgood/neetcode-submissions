class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]

        E = len(edges)
        parents = [i for i in range(E + 1)]
        rank = [1] * (E + 1)

        # 5
        # [0, 1, 2, 3, 4, 5]
        # [1, 1, 1, 1, 1]

        def find(n):
            if n != parents[n]:
                parents[n] = find(parents[n])
            
            return parents[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            # union by rank
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += 1
            else:
                parents[p1] = p2
                rank[p2] += 1
            
            return True
        
        for n1, n2 in edges:
            if union(n1, n2) == False:
                return [n1, n2] # return the last edge in the cycle
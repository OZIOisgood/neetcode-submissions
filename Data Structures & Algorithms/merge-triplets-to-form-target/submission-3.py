class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i in range(0, 3):
                if t[i] ==  target[i]:
                    res[i] = True

                # if t[i] > target[i]:
                #     return False
                
            if all(res):
                return True
        
        return False

        # Time: O(n)
        # Memory: O(n)

        # Tests:
        # 1: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
        # 2: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
        # 3: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]

        # Memory
        # res = [True,True,True]

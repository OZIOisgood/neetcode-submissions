class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [False, False, False]

        for t in triplets:
            if all(t[i] <= target[i] for i in range(3)):
                for i, v in enumerate(t):
                    if v == target[i]:
                        res[i] = True
        
        return all(res)
        
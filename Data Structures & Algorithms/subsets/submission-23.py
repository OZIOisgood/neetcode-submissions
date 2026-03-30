class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums); res = []; path = []

        def bt(i):
            if i == n:
                res.append(path.copy())
                return
            
            path.append(nums[i])
            bt(i + 1)
            path.pop()
            bt(i + 1)
        bt(0)
        return res
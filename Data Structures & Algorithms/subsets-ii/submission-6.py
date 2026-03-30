class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums); res = []; path = []

        def bt(i):
            if i == n:
                res.append(path.copy())
                return
            
            nxt = i + 1
            path.append(nums[i])
            bt(nxt)
            path.pop()

            while nxt < n and nums[nxt] == nums[nxt - 1]: nxt += 1
            bt(nxt)
        bt(0)
        return res
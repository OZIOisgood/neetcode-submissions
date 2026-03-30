class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        
        cur = 0
        for n in nums:
            cur += n
            if cur < 0:
                cur = 0
                continue
            
            res = max(res, cur)
        
        return res
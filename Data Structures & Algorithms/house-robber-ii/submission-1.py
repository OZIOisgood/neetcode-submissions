class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0],
            self.helper(nums[1:]),
            self.helper(nums[:-1]),
        )
        
    def helper(self, nums: List[int]) -> int:
        ll = l = 0
        for n in nums:
            cur = max(ll + n, l)
            ll = l
            l = cur
        return l
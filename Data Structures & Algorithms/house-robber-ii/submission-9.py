class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.help(nums[0:len(nums) - 1]),
                   self.help(nums[1:len(nums)]))

    def help(self, nums: List[int]) -> int:
        ll = 0; l = 0
        for n in nums:
            cur = max(ll + n, l)
            ll = l
            l = cur
        return l
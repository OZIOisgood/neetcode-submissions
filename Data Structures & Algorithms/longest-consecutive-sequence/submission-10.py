class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0; s = set(nums)
        for n in nums:
            l = 0
            while n in s: l += 1; n += 1
            res = max(res, l)
        return res
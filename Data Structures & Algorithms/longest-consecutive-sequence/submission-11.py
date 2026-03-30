class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0; s = set(nums)
        for n in s:
            if (n - 1) not in s:
                l = 0
                while n + l in s: l += 1
                res = max(res, l)
        return res
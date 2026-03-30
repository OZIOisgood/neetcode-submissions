class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in seen: return [seen[k], i]
            seen[n] = i
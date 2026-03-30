class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        realSum = 0; targetSum = 0
        for i, v in enumerate(nums):
            realSum += v
            targetSum += i + 1
        return targetSum - realSum

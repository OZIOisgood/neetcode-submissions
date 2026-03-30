class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum = 0
        initSum = len(nums)

        for i in range(len(nums)):
            numsSum += nums[i]
            initSum += i

        return initSum - numsSum
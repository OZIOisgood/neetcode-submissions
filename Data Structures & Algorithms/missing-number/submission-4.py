class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum = 0
        initSum = len(nums)

        for i in range(len(nums)):
            # print(i)
            numsSum += nums[i]
            initSum += i

        
        print(numsSum)
        print(initSum)

        return initSum - numsSum
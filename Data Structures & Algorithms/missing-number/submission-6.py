class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
            print('----')
            print(res)
            print(i)
            print(nums[i])

        return res
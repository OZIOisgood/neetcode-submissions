class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0

        for i in range(len(nums)):
            print(f"[{i}]: {nums[i]}")

            if nums[i] - 1 in numsSet:
                print(f"{nums[i]} is not a beginning - continue")
                continue
            
            span = 0
            while nums[i] + span in numsSet:
                print(f"{nums[i] + span} is in numsSet - check next")
                span += 1
            
            maxLength = max(
                maxLength,
                span
            )
        
        return maxLength


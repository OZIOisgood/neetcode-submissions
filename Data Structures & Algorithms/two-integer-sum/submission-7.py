class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {
            # [rest = target - num]: rest index
        }

        for i in range(len(nums)):
            goal = target - nums[i]

            if goal in seen:
                return [seen[goal], i]
            else:
                seen[nums[i]] = i

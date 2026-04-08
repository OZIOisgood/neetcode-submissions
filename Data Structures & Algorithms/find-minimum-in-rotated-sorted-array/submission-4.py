class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # already sorted portion
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            # left sorted portion (pivot on the right)
            if nums[l] <= nums[mid]:
                l = mid + 1
            # right sorted portion (pivot on the left)
            else:
                r = mid - 1

        return res
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_index = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
                
                print(nums)
            
            nums[p], nums[r] = nums[r], nums[p]

            if p > k_index:
                return quickSelect(l, p - 1)
            elif p < k_index:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
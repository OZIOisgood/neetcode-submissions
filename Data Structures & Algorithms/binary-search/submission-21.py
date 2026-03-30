class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        
        while l <= r:
            m = (l + r) // 2 # <-- May lead to overflow
            print(f"nums[l]: {nums[l]}; nums[m]: {nums[m]} nums[r]: {nums[r]};")
            print(f"      l: {l};       m: {m};        r: {r};")

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return -1
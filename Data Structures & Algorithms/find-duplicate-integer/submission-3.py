class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        cur = 0
        while True:
            cur = nums[cur]
            if cur in seen: return cur
            seen.add(cur)
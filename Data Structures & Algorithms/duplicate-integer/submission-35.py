class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for _, n in enumerate(nums):
            if n in seen: return True
            seen.add(n)
        return False
class Solution:
    def rob(self, nums: List[int]) -> int:
        ll = l = 0
        for n in nums:
            cur = max(ll + n, l)
            ll = l; l = cur
        return l
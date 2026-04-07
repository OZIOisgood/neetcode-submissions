class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n   = len(nums); firstIdx = 0; lastIndx = n - 1
        a   = [1] * n
        b   = [1] * n
        res = [1] * n

        nxt = 1
        for i, v in enumerate(nums):
            a[firstIdx + i] = nxt
            nxt *= v

        nxt = 1
        for i, v in enumerate(nums[::-1]):
            b[lastIndx - i] = nxt
            nxt *= v
        
        for i in range(n):
            res[i] = a[i] * b[i]

        return res
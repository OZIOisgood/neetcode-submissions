class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for num in numSet:
            # if it is a start of the sequence - increment and capture
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet: length += 1
                res = max(length, res)
        return res
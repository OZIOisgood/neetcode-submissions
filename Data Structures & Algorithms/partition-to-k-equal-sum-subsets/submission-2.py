class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse=True)
        target = total // k
        used = [False] * len(nums)


        def bt(i, k, subsetSum):
            if k == 0: return True
            if subsetSum == target: return bt(0, k - 1, 0)

            for j in range(i, len(nums)):
                nextSum = subsetSum + nums[j]
                if used[j] or nextSum > target: continue
                
                used[j] = True
                if bt(j + 1, k, nextSum): return True
                used[j] = False

                if subsetSum == 0: return False # Pruning
            
            return False
        
        return bt(0, k - 1, 0)

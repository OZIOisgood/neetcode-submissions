class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # subset = []
        def dfs(i, subset):
            print(f"___________")
            print(f"index:  {i}")
            print(f"subset: {subset}")

            if i >= len(nums):
                print(f"done")
                res.append(subset.copy())
                return
            
            # subset.append(nums[i])
            dfs(i + 1, subset + [nums[i]])

            # subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return res
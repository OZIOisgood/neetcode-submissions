class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutes = [[nums[0]]]

        for num in nums[1:]:
            tmp = []
            for permute in permutes:
                for i in range(0, len(permute) + 1):
                    new_permute = permute.copy()
                    new_permute.insert(i, num)
                    tmp.append(new_permute)
            permutes = tmp
        
        return permutes
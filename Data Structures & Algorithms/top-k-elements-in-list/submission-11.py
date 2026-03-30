class Solution:
    def getCountMap(self, nums: List[int]) -> Set[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        return count

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountMap = self.getCountMap(nums)
        print(numCountMap)

        countNumMap = { i: [] for i in range(len(nums) + 1) }
        for num, count in numCountMap.items():
            countNumMap[count].append(num)
        print(countNumMap)

        res = []
        for i in range(len(countNumMap) - 1, 0, -1):
            for num in countNumMap[i]:
                res.append(num)
                if len(res) == k:
                    print(res)
                    return res
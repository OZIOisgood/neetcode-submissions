class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        t = zip(gas, cost)
        cur = 0; start = 0
        for i, (g, c) in enumerate(t):
            cur += g - c
            if cur < 0:
                cur = 0
                start = i + 1
        return start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0: return False
        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        if matchsticks and matchsticks[0] > target: return False

        sides = [0] * 4
        memo = set()

        def dfs(i):
            key = (i, *sorted(sides))
            if key not in memo:
                if i == len(matchsticks): return sides[0] == sides[1] == sides[2] == sides[3]

                for side in range(4):
                    if sides[side] + matchsticks[i] > target: continue
                    sides[side] += matchsticks[i]
                    if dfs(i + 1): return True
                    sides[side] -= matchsticks[i]

                memo.add(key)
            return False

        return dfs(0)

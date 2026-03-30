class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = sorted(list(Counter(tasks).values()), reverse=True)
        maxVal = count[0] - 1
        idleSlots = maxVal * n

        for i in range(1, len(count)): idleSlots -= min(count[i], maxVal)
        return max(idleSlots + len(tasks), len(tasks))
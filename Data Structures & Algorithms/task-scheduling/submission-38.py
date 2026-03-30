class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # find the most freq task
        count                   = Counter(tasks)
        freq                    = sorted(count.values(), reverse=True)
        task_count              = len(freq)
        most_freq_task_count    = freq[0]

        # find idle slots
        number_of_gaps          = most_freq_task_count - 1
        idle_slots              = number_of_gaps * n

        # fill idle slots with other tasks
        for i in range(1, task_count): idle_slots -= min(freq[i], number_of_gaps)
        
        # total time = tasks count + remaining idle slots (if any)
        # if idle_slots goes negative, it means no idles are needed -> answer is just len(tasks)
        return max(idle_slots + len(tasks), len(tasks))

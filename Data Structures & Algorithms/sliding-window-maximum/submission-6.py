class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        l = 0

        for r in range(len(nums)):
            heapq.heappush_max(heap, (nums[r], r))

            # если окно стало больше k, сдвигаем левую границу
            if r - l + 1 > k:
                l += 1

                # выкидываем элементы, которые уже левее окна
                while heap and heap[0][1] < l:
                    heapq.heappop_max(heap)

            # когда окно размера k, фиксируем максимум
            if r - l + 1 == k:
                output.append(heap[0][0])

        return output
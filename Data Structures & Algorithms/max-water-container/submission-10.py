# array.length
# array[i]

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxArea = 0
        while l < r:
            lHeight, rHeight = heights[l], heights[r]
            maxHeight = min(
                lHeight,
                rHeight
            )
            dist = r - l
            area = maxHeight * dist
            maxArea = max(
                maxArea,
                area
            )

            if lHeight <= rHeight:
                l += 1
            else:
                r -= 1


        return maxArea
        # O(n) time, O(1) space
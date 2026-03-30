class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0; r = len(nums) - 1
        
        while l <= r:
            m_idx = l + (r - l) // 2
            m_val = nums[m_idx]
            
            if m_val == target: return m_idx

            left_val = nums[l]; right_val = nums[r]

            # left
            if left_val <= m_val:
                if left_val <= target < m_val:
                    r = m_idx - 1
                else:
                    l = m_idx + 1

            # right
            else:
                if m_val < target <= right_val:
                    l = m_idx + 1
                else:
                    r = m_idx - 1
                
        return -1
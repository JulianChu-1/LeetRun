from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = left = pre_max = suf_max = 0
        right = len(height) - 1

        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])

            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        
        return ans
    
    
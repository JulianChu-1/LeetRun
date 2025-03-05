from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        position = len(nums) - 1
        steps = 0

        while position > 0:
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        
        return steps
    
    def jump2(self, nums):
        n = len(nums)
        if n == 1: return 0

        jumps = 0
        farthest = 0
        end = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                jumps += 1
                end = farthest

                if end >= n - 1:
                    break
        return jumps
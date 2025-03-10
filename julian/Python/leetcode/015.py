from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            j, k = i + 1, n - 1

            if i > 0 and nums[i] == nums[i - 1]: # 防止i重复
                continue

            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while(j < k and nums[j] == nums[j + 1]): # 防止j重复
                        j += 1
                    while(j < k and nums[k] == nums[k - 1]): # 防止k重复
                        k -= 1                   
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return res
            
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = []
        right = []
        left_m, right_m = 1, 1

        for i in range(len(nums)):
            left_m *= nums[i]
            right_m *= nums[(len(nums) - i - 1)]
            left.append(left_m)
            right.append(right_m)
        
        for i in range(len(nums)):
            if i == 0:
                res.append(right[len(nums) - i - 2])
                continue
            if i == len(nums) - 1:
                res.append(left[i - 1])
                break

            res.append(left[i - 1] * right[len(nums) - i - 2])
        
        return res

s = Solution()
print(s.productExceptSelf(nums=[4,3,2,1,2]))
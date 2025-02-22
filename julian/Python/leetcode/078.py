from typing import List


class Solution:
    # 递归回溯
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(nums, index):
            res.append(path[:])

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()
        
        backtrack(nums, 0)

        return res
    
    # 迭代
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [item + [num] for item in res]
        
        return res
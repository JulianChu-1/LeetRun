from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    for i in range(n):
        if nums[i] == 0:
            nums.append(0)
            nums.pop(i)
            i -= 1

nums = [0,0,1]
moveZeroes(nums)
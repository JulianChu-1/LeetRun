#暴力解法 未解决
def removeElement(nums, elements):
    size = len(nums) - 1
    for i in range(size):
        if nums[i] == elements:
            for j in range(i + 1, size):
                nums[j - 1] = nums[j]

print(removeElement([1,2,3,3,4,5], 3))

#快慢指针法 解决
def removeElement1(nums, elements):
    j = 0
    for i in range(len(nums)):
        if nums[i] != elements:
            nums[j] = nums[i]
            j += 1
    return j

'''
    results = [float('inf')] * len(nums)
    j = 0
    for i in range(len(nums)):
        if nums[i] == elements:
            pass
        else:
            results[j] = nums[i]
            j += 1
    return j
'''


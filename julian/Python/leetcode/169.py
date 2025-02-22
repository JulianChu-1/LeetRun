from typing import List


class Solution:
    # 先排序，中间的值一定是众数
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2] 

    # 哈希表
    def majorityElement2(self, nums: List[int]) -> int:
        my_dict = {}
        max_pair = (0, 0)

        for i in nums:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
            if my_dict[i] > max_pair[1]:
                max_pair = (i, my_dict[i])

        return max_pair[0]
    
    # 摩尔投票法
    def majorityElement3(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
            votes += 1 if num == x else -1
        return x
        
s = Solution()
print(s.majorityElement2([3,2,3]))
print(s.majorityElement2([2,2,1,1,1,2,2]))
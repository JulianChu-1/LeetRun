from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        st = set(nums)

        for x in st:
            if x - 1 in st:
                continue
            
            y = x + 1

            while y in st:
                y += 1
            res = max(res, y - x)

        return res


s = Solution()

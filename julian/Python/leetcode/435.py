from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x[1])
        end_point = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if end_point <= intervals[i][0]:
                res += 1
                end_point = intervals[i][1]

        return len(intervals) - res

s = Solution()
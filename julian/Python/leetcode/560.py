from collections import defaultdict
from typing import List

def subarraySum(nums: List[int], k: int) -> int:
    s = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        s[i + 1] = s[i] + x
    
    ans = 0
    cnt = defaultdict(int)

    for sj in s:
        ans += cnt[sj - k]
        cnt[sj] += 1
    
    return ans

def sub2(nums, k):
    ans = s = 0
    cnt = {}
    cnt[0] = 1

    for x in nums:
        s += x

        if (s - k) in cnt:
            ans += cnt[s - k]

        cnt[s] = 1

    return ans
    

print(sub2([-1,-1,1], 0))
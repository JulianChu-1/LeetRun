from typing import List

class Solution:
    def __init__(self):
        self.s = ["h", "e", "l", "l", "o"]

    def reverseString(self, s: List[str]) -> None:
        # 该方法需要额外的O（n）空间
        s[:] = s[::-1]
    
    # 类似于双指针
    def reverseString2(self, s: List[str]) -> None:
        N = len(s)
        for i in range(N // 2):
            s[i], s[N - i - 1] = s[N - i - 1], s[i]

    # 递归
    def reverseString3(self, s: List[str]) -> None:
        def recur(left, right):
            if left >= right:
                return 
            s[left], s[right] = s[right], s[left]
            recur(left + 1, right - 1)
        recur(0, len(s) - 1)

sol = Solution()
sol.reverseString3(sol.s)
print(sol.s)
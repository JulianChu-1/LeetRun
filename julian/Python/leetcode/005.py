class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s

        dp = [[False] * n for _ in range(n)]
        max_len = 1
        begin = 0

        for i in range(n): dp[i][i] = True

        for L in range(2, n + 1):
            for i in range(n): # 左边界
                j = L + i - 1 # 右边界

                if j >= n: break

                if s[i] != s[j]: 
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        
        return s[begin:begin + max_len]
            
s = Solution()
print(s.longestPalindrome('ab'))

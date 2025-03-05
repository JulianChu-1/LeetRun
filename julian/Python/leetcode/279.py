class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            if i ** 0.5 % 1 == 0:
                dp[i] = 1
            else:
                min_count = float('inf')
                for j in range(1, int(i ** 0.5) + 1):
                    min_count = min(min_count, dp[i - j * j])
                dp[i] = 1 + min_count

        return dp[n]

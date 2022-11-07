# Leetcode 338

class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n+1)
        ans = [0]
        for i in range(1, n+1):
            offset = 0
            if offset * 2 == 1:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
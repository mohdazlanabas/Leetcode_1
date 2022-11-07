# Leetcode 424

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = l + count.het(s[r], 0)
            while (r-l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                res = max(res, r -l +1)
        return res
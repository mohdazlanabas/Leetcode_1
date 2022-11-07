# Leetcode 190

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        x : int = 32
        for i in range(x):
            bit = ( n >> i) & 1
            res = res | (bit << ((x-1) - i))
        return res

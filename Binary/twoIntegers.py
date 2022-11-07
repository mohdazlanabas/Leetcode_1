# Leetcode 371

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        MSK = 0xFFFFFFFF
        carry = (a&b) << 1
        out = a ^ b

        carry &= MSK
        out &= MSK

        if carry != 0:
            return self.getSum(out, carry)
        else:
            if out < MAX:
                return out
            else:
                return ~(out ^ MSK)
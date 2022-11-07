# Leetcode 53

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = (maxSub, curSum)
        return maxSub

        
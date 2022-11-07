# Leetcode 128

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            length = 0
            if (n-1) not in numSet:
                while (n + length) in numSet:
                    length += 1
            longest = max(length, longest)
        return longest
# Leet code 15
class Solution:
    def threesome(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left, right= i +1, len(nums) -1
            while left < right:
                threesome = a + nums[left] + nums[right]
                if threesome > 0:
                    right -= 1
                elif threesome < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                        return result
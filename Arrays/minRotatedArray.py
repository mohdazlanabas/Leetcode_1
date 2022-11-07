# Leetcode 153

class Solution2:
    def findMin(self, nums: list[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            left =0
            right = len(nums) - 1
            if nums[right] > nums[0]:
                return nums[0]
            while right >= left:
                mid = left + (right - left) // 2 # // is floor division
                if nums[mid] > nums[mid +1]:
                    return nums[mid +1]
                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                if nums[mid] > nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1

    class Solution2:
        def findMin(self, nums: list[int]) -> int:
            result = nums[0]
            l, r=0, len(nums) -1
            while l <= r:
                if nums[l] < nums[r]:
                    result = min(result, nums[l])
                    break
                m = (l + r) // 2
                result = min(result, nums[m])
                if nums[m] >= nums[l]:
                    l = m +1
                else:
                    r = m +1
                return result
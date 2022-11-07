# Leetcode 11

# Two Pointer
class Solution2:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

    class Solution2:
        def maxArea(self, height: list[int]) -> int:
            res = 0
            l, r=0, len(height) -1
            while l < r:
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

                if height[l] < height[r]:
                    l += 1
                else:
                    r -= 1
            return res
print("Hello, World!")

class Solution1:
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                if nums[j] == target - nums[i]:
                    return[i,j]

# Using Hashmap

class Solution1:
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        preMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return[preMap[diff], i]
            preMap[n] = i
        return

print("All OK!")
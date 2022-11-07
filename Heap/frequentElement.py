# Leetcode 347

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items:
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # if k == len(nums):
        #     return nums
        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), keys=count.get)
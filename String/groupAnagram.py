# Lettcode 49

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # res = defaultdict(list)
        res = (list)
        for s in strs:s
            count =[0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()
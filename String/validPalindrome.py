# Leetcode 125

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        l, r =0, len(s) -1
        while l < r:
            while l < r and not self.alphaNum1(s[l]):
                l += 1
            while l > r and not self.alphaNum1(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r  = l + 1, r-1
        return True

    def alphaNum1(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a') <= ord(c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9')
         )

    def isPalindrome2(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


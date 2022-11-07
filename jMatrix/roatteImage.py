# Leetcode 48

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r =0, len(matrix) -1
        while l < r:
            for i in range(r-l):
                top, bottom = l,r
                tapper = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom-i][l]
                matrix[bottom][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top + i][r]
                matrix[top +i][r] = tapper
            r -= 1
            l += 1
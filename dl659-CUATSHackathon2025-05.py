# 78. Subsets
# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            size = len(subsets)
            for y in range(size):
                subsets.append(subsets[y] + [num])

        return subsets

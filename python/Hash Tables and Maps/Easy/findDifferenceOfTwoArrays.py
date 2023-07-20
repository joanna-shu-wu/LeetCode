"""
Returns the elements in the first arg nums1 that don't exist in the second arg nums2
We are given two integer arrays, nums1 and nums2, and need to return a list of two lists. 
"""
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set(nums1)
        num2 = set(nums2)

        arr1 = [x for x in num1 if x not in num2]
        arr2 = [x for x in num2 if x not in num1]

        return [arr1, arr2]

sol = Solution()
print(sol.findDifference([1, 2, 3], [2, 4, 6]))

"""
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
"""
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2  # Sum of numbers from 1 to n
        actual_sum = sum(nums)
        missing_number = expected_sum - actual_sum
        return missing_number
            
sol=Solution()
print(sol.missingNumber([3,0,1]))
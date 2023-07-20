"""
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''  nums.sort()
        result=[]
        for idx,num in enumerate(nums):
            if idx+1!=num:
                result.append(idx+1)
        return result
        '''
        set_nums = set(nums)
        result=[]
        for num in range(1,len(nums)+1):
            if num not in set_nums:
                result.append(num)
        return result

code=Solution()

print(code.findDisappearedNumbers([1,1]))
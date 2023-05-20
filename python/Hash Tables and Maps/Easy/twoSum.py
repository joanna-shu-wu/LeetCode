'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''
# keys: element
# values: index
# [3,6,12,14]
# map: [<3,0>,<6,1>,<12,2>]
# x+y= target; y=current number, target=input => x=target-y
# If we've seen x before, that means we just need to return the indice of x and y

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i in range(len(nums)):
            x=target-nums[i] #nums[i] is the current value in the loop
            if x in m:#check if the goal is a key in the map
                return [m[x],i]
            m[nums[i]]=i #assing the key as current element and assign the as value as current index for later iteration

sol=Solution()
inputArray=[1,2,3,4]
target=4
result=sol.twoSum(inputArray,target)
print(result)


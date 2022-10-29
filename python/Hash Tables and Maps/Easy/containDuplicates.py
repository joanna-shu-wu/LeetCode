'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

'''
#Method 1: sort the array, pass over the array once. If two consecutive elements are the same ,return true
#Method 2:Add all elements in a set. Then compare set size and array size. If the size are the same, return true 
#**Method 3: Use hashamp. Create a map. Loop over the array. Within the loop, check if current element exist in the map. If it does, return true; if not, update the map with current element 

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m=defaultdict(int)
        for num in nums:
            if(m[num]):
                return True 
            m[num] +=1 # Add num to the key of the map, 1 as the value of the map
        return False
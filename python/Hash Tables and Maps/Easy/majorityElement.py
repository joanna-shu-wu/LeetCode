'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

'''

# Use map where keys are the elements and the values are the occurence count.
# Time complexity is O(2*N) = O(N) because there are two loops
# Space complexity is O(N) because we create a map that holds the input array elements along with the no. of occurance of each element


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m={}
        for num in nums: # this loop add the num in the list nums to the map m
            m[num]=m.get(num,0)+1

        for num in nums:
            if(m[num]>len(nums)//2): # this loop check the occurance frequency of the num in the map 
                return num
                



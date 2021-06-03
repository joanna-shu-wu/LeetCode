''''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr)<3): # Return False  becasue it's not possible to form a mountain if the length of the array has only 1 or 2 elements
            return False
        i=1
        while(i<len(arr) and arr[i]>arr[i-1] ): # check the increasing hill
            i+=1
        if(i==1 or i==len(arr)): # Return False if there's no increasing hill (i==1) or no decreasing hill (i=len(arr))
            return False

        while(i<len(arr) and arr[i]<arr[i-1]): # check the decreasing hill
            i+=1
        return i==len(arr) # Check if we reached the end of the array. We want the decreasing hill reach the end of the array

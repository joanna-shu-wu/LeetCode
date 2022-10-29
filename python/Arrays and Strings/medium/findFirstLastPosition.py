'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

'''
# Finding first occurance index
# 1. Init 2 pointers. One at the start of the array, one at the end
# 2. Find the middle between the two pointers
# 3. Use if statement to check if the mid is the same as the target 
# 4. Use if statement to check if the it is the first occurence of that element

# Finding last occurance index


class Solution:
    
    
    def getLeftPosition(self,nums,target):
        left =0
        right = len(nums)-1
        while(left<=right):
            mid =(left+right)//2
            if(nums[mid]==target):
                if(mid-1>0 and nums[mid-1]!=target or mid==0):
                    return mid
                right=mid-1 # if haven't found mid yet, update the right pointer to continue to search. We narrow down the search range from left to one element before mid
            elif(nums[mid]>target):
                right = mid-1 # the target must exist before the current mid. So we set the upper search bound at one element before the mid
            else:
                left = mid+1 # the target is bigger than the current mid. So we set the lower search bound at one element afer the mid
        return -1 # we didn't find the element at all
    
    def getRightPosition(self,nums,target): 
        left =0
        right = len(nums)-1
        while(left<=right):
            mid =(left+right)//2 # the mid at getRightPosition needs to be the last target number
            if(nums[mid]==target):
                if(mid+1<len(nums) and nums[mid+1]!=target or mid==len(nums)-1): # the element after mid is not equal to the target or the mid is at the last position of the array
                    return mid
                left=mid+1 # the target must have another position that come after mid. So we set the lower search bound to be one element after mid
            elif(nums[mid]>target):
                right = mid-1
            else:
                left = mid+1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.getLeftPosition(nums,target)
        right = self.getRightPosition(nums,target)
        
        return [left, right]
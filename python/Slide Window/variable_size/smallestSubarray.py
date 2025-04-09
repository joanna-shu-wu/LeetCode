'''
Question:
Given an array and a target, 
find the smallest subarray that sum equal or greater than the target

Hint: This is the dynamic window question
dynamic slide window recipe:
must: initial result, initial the beginning of the window, 
then for+while, the end of the window is the variable in for loop
optional: initial temp container/variable
'''

def minSubArrayLen( nums, target):
    left = 0
    total = 0
    min_len = float('inf')  # Initialize with a large number

    for right in range(len(nums)):
        total += nums[right]  # Expand the window

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]  # Shrink the window
            left += 1

    return 0 if min_len == float('inf') else min_len


print(minSubArrayLen(7, [2,3,1,2,4,3]))
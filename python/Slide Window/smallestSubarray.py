'''
Question:
Given an array and a target, find the smallest subarray that sum equal or greater than the target

Hint: This is the dynamic window question
dynamic slide window recipe:
must: initial result, initial the beginning of the window, then for+while, the end of the window is the variable in for loop
optional: initial temp container/variable
'''

def minSubArrayLen( s, nums):
    minWindowSize = float("inf") #initial result # 定义一个无限大的数
    currentWindowSum = 0 
    windowStart = 0 
    for windowEnd in range(len(nums)): #i is the end of the window
        currentWindowSum += nums[windowEnd]
        while currentWindowSum >= s:
            minWindowSize = min(minWindowSize,windowEnd-windowStart+1)
            currentWindowSum -= nums[windowStart]
            windowStart += 1
    return 0 if minWindowSize==float("inf") else minWindowSize


print(minSubArrayLen(7, [2,3,1,2,4,3]))
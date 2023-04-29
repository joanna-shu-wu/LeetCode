'''
slide window recipe:
must: initial result, initial the beginning of the window, then for+if/while, the end of the window is the variable in for loop
optional: initial temp container/variable
'''
def minSubArrayLen( s, nums):
    # 定义一个无限大的数
    res = float("inf") #initial result
    Sum = 0  #initial temp container/variable
    index = 0 #index is the beginning of the window
    for i in range(len(nums)): #i is the end of the window
        Sum += nums[i]
        while Sum >= s:
            res = min(res, i-index+1)
            Sum -= nums[index]
            index += 1
    return 0 if res==float("inf") else res


print(minSubArrayLen(7, [2,3,1,2,4,3]))
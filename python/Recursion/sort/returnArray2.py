'''
Given an array of number and target number, return the array of index of where the target is
example: given [1,2,3,4,4,5,6], target=4, return [3,4]
Method 2: don't pass the list as the paramater
Hint: include the below function return value to the current function
'''

def findTargetIndex(array,target):
    return helper(array,target,0) 


def helper(array,target,index):
    result_array=[]
    if index==len(array)-1:
        return result_array
    if array[index]==target:
        result_array.append(index)

    last_function_result=helper(array,target,index+1) #this line is key. This variable incorporate the result from last function call to the current function call
   
    result_array.extend(last_function_result)
    return result_array

print(findTargetIndex([1,2,3,4,4,5,6],4))
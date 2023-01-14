'''
Given an array of number and target number, return the array of index of where the target is
example: given [1,2,3,4,4,5,6], target=4, return [3,4]
'''
from unittest import result


def findTargetIndex(array,target):
    return helper(array,target,0)

def helper(array,target,index):
    result_array=[]
    if index==len(array)-1:
        return result_array
    if array[index]==target:
        return result_array.append(index)
    helper(array,target,index+1)
     

print(findTargetIndex([1,2,3,4,4,5,6],4))
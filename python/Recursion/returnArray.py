'''
Given an array of number and target number, return the array of index of where the target is
example: given [1,2,3,4,4,5,6], target=4, return [3,4]
'''
from unittest import result


def findTargetIndex(array,target):
    return helper(array,target,0,[]) # the [] is the reference variable. It creates a new ref variable during each method call. They all point to the same object


def helper(array,target,index,result_array):
    if index==len(array)-1:
        return result_array
    if array[index]==target:
        result_array.append(index)
    return helper(array,target,index+1,result_array) # return every function call so that the ref variable can be pass all the way back
     

print(findTargetIndex([1,2,3,4,4,5,6],4))

"""  (option+shift+a to comment multiple lines)
Stack Fame
helper([1,2,3,4,4,5,6],4,6,[3,4])
helper([1,2,3,4,4,5,6],4,5,[3,4])
result_array.append(4)
helper([1,2,3,4,4,5,6],4,4,[3])
result_array.append(3)
helper([1,2,3,4,4,5,6],4,3,[])
helper([1,2,3,4,4,5,6],4,2,[])
helper([1,2,3,4,4,5,6],4,1,[])
helper([1,2,3,4,4,5,6],4,0,[])
 """

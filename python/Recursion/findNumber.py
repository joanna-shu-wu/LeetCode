""" def find(array, target,index):
    if index==len(array):
        return False
    return array[index]==target or find(array, target, index+1)
 """

def find(array, target):
    index=0
    return helper(array, target,index)
    
def helper(array, target,index):
    if index==len(array):
        return False
    return array[index]==target or helper(array, target, index+1)

print(find([5,1,7,3,5],1))
'''Given an array, check if it's sorted'''

def sorted(array):
    index=0
    return helper(array, index)

def helper(array, index):
    if index==len(array)-1:
       return True # when the index reach the last element, it has nothing to compare with, so just return true
    return array[index]<array[index+1] and helper(array,index+1)

print(sorted([1,2,3,4,5,6]))
'''
([1,2,3,4,5,6],0), len(array)-1=6-1=5
1<2 and ([2,3,4,5,6],1)                         
         2<3 and ([3,4,5,6],2)                     ^          
                  3<4 and ([4,5,6],3)              ^
                            4<5 and ([5,6],4)      ^
                                     5<7 and True  ^
'''
print(sorted([4,3,2,1]))
'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


'''


from typing import List


class Solution:
    def solution(self, nums,ans,cur,index):
        if(index>len(nums)):
            return
        ans.append(cur[:])
        for i in range(index,len(nums)):
            if(nums[i] not in cur):
                cur.append(nums[i])
                self.solution(nums, ans,cur,i)
                cur.pop()
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]
        self.solution(nums,ans,cur,0)
        return ans

#https://www.youtube.com/watch?v=REOH22Xwdkk
def subset(array):
    result=[] #it has global access for the dfs function
    subset=[] #it has global access for the dfs function
    def dfs(index):
        if index>=len(array): #base case
            result.append(subset.copy()) #we are at the leaf node so we add the copy of the subset
            return #return because it is out of bound
        
        #To include array[i], it's the left branch of the decision tree
        subset.append(array[index])
        dfs(index+1)

        #Not to include array[i]. We pop the element we just appened
        subset.pop()
        dfs(index+1)
    dfs(0)
    return result

print(subset([1,2,3]))
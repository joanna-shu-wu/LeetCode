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
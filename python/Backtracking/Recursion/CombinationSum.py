'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
'''


class Solution:
    def solution(self, candidates, ans,cur,target,index,sum):
        if(sum==target):
            ans.append(cur[:])
        elif(sum<target):#we need to add more element from the list
            n=len(candidates)
            for i in range(index, n):
                cur.append(candidates[i])
                self.solution(candidates,ans,cur,target,i,sum+candidates[i])
                cur.pop()
        return
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        cur=[]
        self.solution(candidates,ans,cur,target,0,0)


        return ans
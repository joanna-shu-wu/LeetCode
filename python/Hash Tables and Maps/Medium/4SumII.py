'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0


Example
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

'''


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m={}
        ans=0
        sA=len(nums1)
        sB=len(nums2)
        sC=len(nums3)
        sD=len(nums4)

        for i in range(0,sA):
            x=nums1[i]
            for j in range(0,sB):
                y=nums2[j]
                if(x+y not in m):
                    m[x+y]=0
                m[x+y]+=1

        for i in range(0,sC):
            x=nums3[i]
            for j in range(0,sD):
                y=nums4[j]
                target=-(x+y)
                if(target in m):
                    ans+=m[target]
        return ans

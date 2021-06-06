# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left =1
        right =n
        
        while(left<right):
            mid = (left+right)//2
            if(not isBadVersion(mid)):
                left = mid+1 #if the current mid is not bad, that means the bad version is after the current mid. We added 1 to move the pointer after mid to continue to search
            else: #the bad version is before the mid. So we set the upper search bound to the mid
                right = mid 
        return left
                
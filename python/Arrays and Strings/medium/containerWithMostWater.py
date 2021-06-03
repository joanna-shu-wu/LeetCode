'''

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

'''

# Real question is to find the max width (difference between x position) multiplied by the height (value)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area =0
        while(l<r):#loop as long as the right pointer is smaller than the left pointer
            max_area = max(max_area, min(height[l],height[r])*(r-1)) # Find if we can get a bigger area by finding the min between the two building being pointed. Then multiply by the width
            if(height[l]<height[r]): #Optimize the pointer position for the next iteration to max the area. We do so by moving the pointer with the smaller height
                l+=1 # move the left pointer if its value is smaller than the value pointed by the right pointer
            else:
                r-=1 # move the right pointer if its value is smaller than the value pointed by the left pointer
        return max_area
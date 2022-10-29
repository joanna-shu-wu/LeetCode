'''

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

'''

# If current element is bigger than the previous element by more than 1, the missing number is the current element -1
# The quick sort and merge sort are Nlog(N). To be optimal, we can use hashmap
# Hashmap: loop over the array, set current element as true in the map. Loop from 0 to n, check if current element is not set to true in the hashmap
# Gauss method: n(1+n)/2. Intended sum - current sum = missing value. Time complexity is O(N), space complexity is O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       currentSum = sum(nums)
       n= len(nums) # it helps to get the intended sum
       intendedSum = n*(n+1)/2
       return int(intendedSum-currentSum) 
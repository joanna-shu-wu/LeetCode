'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

def longestConsecutiveSeq(arry):
    arry.sort()
    l=0
    for idx in range(len(arry)-1):
        if arry[idx]+1==arry[idx+1]:
            l+=1
    return l+1



print(longestConsecutiveSeq([100,4,200,1,3,2]))


#without using sort
def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest

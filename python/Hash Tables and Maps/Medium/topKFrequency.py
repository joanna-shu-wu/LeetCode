'''
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
from collections import defaultdict

def topKFrequent(nums,k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] =1+count.get(n, 0) #{5:3,4:2,9:1,7:1,6:1}
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

print(topKFrequent([5,5,4,9,7,6,5,4], 2))
'''
Given an array of integers, partition the array into two subsets such that:
1. The sum of the elements in both subsets is equal.
2. Return all the elements in the partition (combined), sorted or in any order.
3. If it's not possible, return -1.

Step	                       Technique	             Why It's Greedy
Sort the array	            Greedy heuristic	      Sorting to force structure.
Pair numbers alternately   	Immediate local choice	No backtracking.
Check sum equality	        Hope it works	          No guarantee.
'''


def ArrayChallenge(arr):

  # code goes here
  total_sum=sum(arr)
  
  target_sum=total_sum/2
  
  arr.sort()

  set1=set()
  set2=set()

  for num1, num2 in zip(arr[::2],arr[1::2]):
    set1.add(num1)
    set2.add(num2)

  if set1!=target_sum or set2!=target_sum :
    return -1

  result=','.join(str(num) for num in set1.union(set2))
  return result

print(ArrayChallenge([16, 22, 35, 8, 20, 1, 21, 11]))
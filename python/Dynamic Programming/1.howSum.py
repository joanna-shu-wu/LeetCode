# Recursive. Time: O(n^m*m) | Space:O(m) where m is the tagetSum, n is numbers
# it's the tree with m height, each edge is the number, each node is the number of the parent node minus the number of the edge 
# Input tagetSum is a integer, numbers is an array of integer
# if cannot add up, return null
def howSum(tagetSum, numbers):
    if targetSum==0:
        return []
    if targetSum<0:
        return null
    # branching logic    
    for num in numbers:
        remainder=targetSum-num
        remainderResult=howSum(remainder,numbers)
        if remainderResult is not None: # if it enters this if statement, it means it has a chance to sum up to the target
            return remainderResult.append(num) # add the number on the edge
    return null

# Dynamic programming
def howSum(tagetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]
    if targetSum==0:
        return []
    if targetSum<0:
        return null
    # branching logic    
    for num in numbers:
        remainder=targetSum-num
        remainderResult=howSum(remainder,numbers,memo)
        if remainderResult is not None: # if it enters this if statement, it means it has a chance to sum up to the target
            memo[targetSum]=remainderResult.append(num) # note:the value of the targetSum is a number of array
            return memo[targetSum] # add the number on the edge
    memo[targetSum]=null
    return null
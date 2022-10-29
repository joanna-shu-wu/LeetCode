# bestSum(7,[5,3,4,7]), the best sum is 7
# bestSum(8,[2,3,5]), the best sum is [3,5], not [2,2,2,2]
# Recursive. Time: O(n^m*m) | Space:O(m) 
def bestSum(targetSum, numbers):
    if targetSum==0:
        return []
    if targetSum<0:
        return null

    shortestCombination=null

    for num in numbers:
        remainder=targetSum-num
        remainderCombination=best(remainder,numbers)
        if remainderCombination is not None:
            combination=remainderCombination.append(num)
            #if the combination is shorter than the current shortest, update it
            if shortestCombination=null or len(combination)<len(shortestCombination):
                shortestCombination=combination

    return shortestCombination # the return is no longer in the loop because we need to explore all posibility to find the best combination so w




def bestSum(targetSum, numbers,memo={}):
    if tagetSum in memo.keys():
        return memo[targetSum]
    if targetSum==0:
        return []
    if targetSum<0:
        return null

    shortestCombination=null

    for num in numbers:
        remainder=targetSum-num
        remainderCombination=best(remainder,numbers,memo)
        if remainderCombination is not None:
            combination=remainderCombination.append(num)
            #if the combination is shorter than the current shortest, update it
            if shortestCombination=null or len(combination)<len(shortestCombination):
                shortestCombination=combination

    memo[targetSum]=shortestCombination
    return shortestCombination # the return is no longer in the loop because we need to explore all posibility to find the best combination so w

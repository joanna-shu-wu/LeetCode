# Recursive. Time: O(n^m) | Space:O(m) where m is the tagetSum, n is numbers
# it's the tree with m height, each branch has n nodes
# Input tagetSum is a integer, numbers is an array of integer
def canSum(tagetSum, numbers):
    if tagetSum==0:
        return True
    if targetSum<0:
        return False

    for num in numbers:
        remainder=tagetSum-num
        if canSum(remainder,numbers)== True:
            return True
    return False # return False after the for loop. It's because after you attmepted every possibilty and nothing work out, I then say False


# Dynamic programming by using memoize
# Complexity: Time: O(n*m) | Space:O(m)
def canSum(tagetSum, numbers, memo={}):
    if tagetSum in memo.keys():
        return memo[targetSum]
    if tagetSum==0:
        return True
    if targetSum<0:
        return False

    for num in numbers:
        remainder=tagetSum-num
        if canSum(remainder,numbers,memo)== True:
            memo[targetSum]=True
            return True
    memo[targetSum]=False
    else:
        return False
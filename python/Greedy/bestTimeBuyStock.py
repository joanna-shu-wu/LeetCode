'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

'''
slide window recipe: initial result,initial the beginning of the window,, then for+if/while
Sliding window uses one pointer and one variable for the window size to find a window within the sequence.
'''
# Joanna solution. It's wrong. 
def bestTimeBuyStock(arr):
    maxProfit=0 #initial result
    l=0 #initial the beginning of the window,
    for l in range(len(arr)): #update the pointer to a new location
        for r in range(len(arr)):
            while arr[r]<arr[l]:
                break
            maxProfit=max(maxProfit,arr[r]-arr[l])
        l=+1
    return maxProfit

# Real solution
def maxProfit(arry) -> int:
    res = 0
    l = arry[0]
    for r in arry:
        if r < l:
            l = r
        res = max(res, r - l)
    return res

def main():
    print(bestTimeBuyStock([7,1,5,3,6,4]))
    print(maxProfit([7,1,5,3,6,4]))
#[3,2,12,6], 

if __name__=='__main__':
    main()


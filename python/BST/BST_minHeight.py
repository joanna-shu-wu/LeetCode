'''
Write a function that take in a non-empty sorted array of distinct integers.The function should minimized the height of BST
'''

#method 1: naive insert implementation
# O(Nlog(N)) time | O(n) space
def minHeightBst(array):
    return constructMinHeightBst(array,None, 0,len(array)-1) # pass None because there's no bst yet 

def constructMinHeightBst(array,bst, startIdx,endIdx):
	if endIdx<startIdx: #base case: it runs out of value in the subtree
		return None   
	midIdx=(startIdx+endIdx) // 2 #round down
	valueToAdd=array[midIdx]
    if bst is None:
        bst=BST(valueToAdd) # root node	    
	else:
        bst.insert(valueToAdd)
    #Once we are done with creating or inserting BST node, we call the function itself for the remaining subarray
    constructMinHeightBst(array,bst, startIdx,midIdx-1)
    constructMinHeightBst(array,bst, midIdx+1,endIdx)
	return bst


#method 2
# O(N) time | O(n) space
def minHeightBst(array):
    return constructMinHeightBst(array,0,len(array)-1)

def constructMinHeightBst(array,startIdx,endIdx):
	if endIdx<startIdx: #base case: it runs out of value in the subtree
		return None
    
	midIdx=(startIdx+endIdx) // 2 
	bst=BST(array[midIdx]) # manually create a bst at every recursive call
	bst.left=constructMinHeightBst(array,startIdx,midIdx-1)
	bst.right=constructMinHeightBst(array,midIdx+1,endIdx)
	return bst # use return to populate bst






class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

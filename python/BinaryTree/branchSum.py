'''Write a function that takes in a Bibary Tree and return a list of its branches
sums ordered from the leftmost branch to the rightmost branch'''


# O(n) time: traverse all the nodes | 0(n) space. Only (log n) in the call stack, n/2 of leaf node in the sums list
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
	sums=[]
	branchSumsHelper(root,0,sums)
    return sums


# need to keep track of the runningSum and sums list
def branchSumsHelper(node,runningSum,sums):
	if node is None: #the base case
		return

	newRunningSum=runningSum+node.value #runningSum is the sum of all the previous nodes
	
	if node.left is None and node.right is None: # when reach the leaf node, append the newRunningsum to the sums list
		sums.append(newRunningSum)
		return
	
	branchSumsHelper(node.left,newRunningSum,sums)
	branchSumsHelper(node.right,newRunningSum,sums)
	
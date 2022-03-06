'''
Write a function that take in a BST and a positive integer K and returnsthe kth largest
'''
#------------------------------------------------------------------------------------------------------+
# Method 1: O(n) time | O(n) space - where n is the number of the node
#------------------------------------------------------------------------------------------------------+
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    sortedNodeValues=[]
	inOrderTraverse(tree,sortedNodeValues)
	return sortedNodeValues[len(sortedNodeValues)-k]

def inOrderTraverse(node,sortedNodeValues):
	if node is None: # base case.
		return
	
	inOrderTraverse(node.left,sortedNodeValues)
	sortedNodeValues.append(node.value)
	inOrderTraverse(node.right,sortedNodeValues)


#------------------------------------------------------------------------------------------------------+
# Method 2: O(h+k) time | O(h) space - where h is the height of the tree and k is the input parameter 
#------------------------------------------------------------------------------------------------------+

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo: #store the numberOfNodesVisited and lastVisitedNodeValue in the class
	def __init__(self,numberOfNodesVisited,lastVisitedNodeValue):
		self.numberOfNodesVisited=numberOfNodesVisited
		self.lastVisitedNodeValue=lastVisitedNodeValue
		
def findKthLargestValueInBst(tree, k):
    treeInfo=TreeInfo(0,-1) #-1 means there's no value yet
	reverseInOrderTraverse(tree,k,treeInfo)
	return treeInfo.lastVisitedNodeValue

def reverseInOrderTraverse(node,k,treeInfo):
	if node is None or treeInfo.numberOfNodesVisited>=k:
		return
	
	reverseInOrderTraverse(node.right,k,treeInfo)
	if treeInfo.numberOfNodesVisited<k:
		treeInfo.numberOfNodesVisited+=1
		treeInfo.lastVisitedNodeValue=node.value
	reverseInOrderTraverse(node.left,k,treeInfo)
	
	
	
	
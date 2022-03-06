'''
Write a function that take in a BST and returns the sum of its node depth
'''

#------------------------------------------------------------------------------------------------------+
# Method 1: O(n) time | O(h) space - where n is the number of the node, h is the height of the tree
#------------------------------------------------------------------------------------------------------+

def nodeDepths(root, depth=0):
	sumOfDepths=0
	stack=[{"node":root,"depth":0}]
	while len(stack)>0:
		nodeInfo=stack.pop()
		node,depth=nodeInfo["node"],nodeInfo["depth"]
		if node is None:
			continue
		sumOfDepths+=depth
		stack.append({"node":node.left,"depth":depth+1})
		stack.append({"node":node.right,"depth":depth+1})
	return sumOfDepths

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

		
	


#------------------------------------------------------------------------------------------------------+
# Method 2: O(n) time | O(h) space - where n is the number of the node, h is the height of the tree
#------------------------------------------------------------------------------------------------------+

def nodeDepths(root, depth=0):
	if root is None:
		return 0
    return depth+nodeDepths(root.left,depth+1)+nodeDepths(root.right,depth+1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

		
	
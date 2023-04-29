class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
'''
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
Traverse the left subtree, i.e., call Inorder(left->subtree)
Visit the root.
Traverse the right subtree, i.e., call Inorder(right->subtree)
'''
def inOrderTraverse(tree, array):
	if tree is not None:
		inOrderTraverse(tree.left,array)
		array.append(tree.value)
		inOrderTraverse(tree.right,array)
	return array

if __name__ == "__main__":
  root = BST(1)
  root.left = BST(2)
  root.right = BST(3)
  root.left.left = BST(4)
  root.left.right = BST(5)
'''
		1 <60>
	2<40>		3<70>
4<00>       5<30>
inOrderTraverse output [4, 2, 5, 1, 3]
'''

  # Function call
print("Preorder traversal of binary tree is")
print(inOrderTraverse(root,[]))

def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left,array)
		preOrderTraverse(tree.right,array)
	return array



def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left,array)
		postOrderTraverse(tree.right,array)
		array.append(tree.value)
	return array

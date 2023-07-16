

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        temp=root.left
        root.right=root.left
        root.left=temp

        self.invertTree(root.left)
        self.invertTree(root.right) 

        return root


# Create a binary tree
#        4
#       / \
#      2   7
#     / \ / \
#    1  3 6  9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Create an instance of Solution class
solution = Solution()

# Invert the binary tree
inverted_root = solution.invertTree(root)

# Print the inverted binary tree (pre-order traversal)
def print_tree(node):
    if node is None:
        return
    print(node.val, end=" ")
    print_tree(node.left)
    print_tree(node.right)


print_tree(inverted_root)
# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        pass
	
	# keep trakc of the parentNode
    def remove(self, value,parentNode=None):
       #step 1: find the value that need to be removed
		currentNode=self
		while currentNode is not None:
			if value<currentNode.value:
				parentNode=currentNode
				currentNode=currentNode.left
			elif value>currentNode.value:
				parentNode=currentNode
				currentNode=currentNode.right
			# Step 2: bread and butter. Once find the value, remove it
			else:
				# case 1: the removed value has two child nodes
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value=currentNode.right.getMinValue()
					currentNode.right.remove(currentNode.value,currentNode)
				# case 2: the removed value is the root node
				elif parantNode is None:
					if currentNode.left is not None:
						currentNode.value=currentNode.left.value
						currentNode.right=currentNode.left.right
						currentNode.left=currentNode.left.left
					elif currentNode.right is not None:
						currentNode.value=currentNode.right.value
						currentNode.right=currentNode.right.right
						currentNode.left=currentNode.right.left
					# single node tree. do nothing
					else:
						pass
				# case 3: the removed value has only one child node
				elif parentNode.left==currentNode:
					parentNode.left=currentNode.left if currentNode.left is not None else currentNode.right
					
				
				
				
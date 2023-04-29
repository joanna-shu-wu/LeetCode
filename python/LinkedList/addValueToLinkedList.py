"""
Input is a linkeklist. Output an array that contains all the values in the linkedlist
"""
class Node:
   def __init__(self, val):
      self.val = val
      self.next = None


def addValueToArray(head):
    result=[]
    current=head
    while current is not None:
        result.append(current.val)
        current=current.next
    return result

def addValueToArrayRecursion(head,arry):
    if head is None:
        return arry
    arry.append(head.val)
    return addValueToArrayRecursion(head.next,arry)
 
def addValueToArrayRecursion2(head,arry):
    if head is not None:
        arry.append(head.val)
        addValueToArrayRecursion(head.next,arry)
    return arry

def addValueToArrayRecursionHelper(head):
    arry=[]
    fillvalue(head,arry)
    return arry

def fillvalue(head,arry):
    if head is None:
        return 
    arry.append(head.val)
    addValueToArrayRecursionHelper(head.next,arry)
 

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next=b
b.next=c
c.next=d
d.next=e

#print(addValueToArray(a))
#print(addValueToArrayRecursion(a,[]))
print(addValueToArrayRecursion2(a,[]))
#print(addValueToArrayRecursionHelper(a))
class Node:
   def __init__(self, val):
      self.val = val
      self.next = None

def travesal(head):
    current=head
    while current is not None:
        print(current.val)
        current=current.next


def travesalRecursive(head):
    if head is None:
        return
    print(head.val)
    travesalRecursive(head.next)

        

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.next=b
b.next=c
c.next=d
d.next=e

travesal(a)
#travesalRecursive(a)

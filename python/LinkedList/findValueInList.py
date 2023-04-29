class Node:
   def __init__(self, head=None):
      self.head = head
      self.next = None

def findValue(list, index):
    current=list[0]
    while index !=0:
        for i in range(len(list)):
            if current==list[i]:
                return index
        index-=1

def findValueRecursive(list, index):
    if list[index]==list.value:
        return list.value
    return findValueRecursive(list.next,index)

print(findValue([1,2,3,4,5],3))

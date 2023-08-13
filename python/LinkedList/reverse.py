# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Use two pointers technique'''
        prev,curr=null,head #two pointers call prev and curr
        # 1->2->3
        while curr: #while curr is not null
            nxt=curr.next #save 2 to nxt before breaking the link between 1 and 2
            curr.next=prev #break the link between 1 and 2 by pointing to prev
            prev=curr #move prev
            curr=nxt
        return prev

solution = Solution()
# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

reversed_head = solution.reverseList(node1)

'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
'''

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur=ListNode(0)
        ans=cur #this would always point to the head of the newly sorted list

        while(l1 and l2): #start looping through two input lists
            if(l1.val>l2.val):
                cur.next=l2  # the smaller node is appended to the end of the list
                l2=l2.next #move the pointer of l2 to point to the next node
            else:
                cur.next=l1
                l1=l1.next

            cur=cur.next #have the cur always point to the last node
        while(l1):
            cur.next=l1
            l1=l1.next
            cur=cur.next

        while(l2):
            cur.next=l2
            l2=l2.next
            cur=cur.next
        return ans.next

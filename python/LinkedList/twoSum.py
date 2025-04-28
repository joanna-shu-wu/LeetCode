'''
You’re given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            # Move forward
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next


# Helper function to build a linked list from a list of values
def build_list(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


l1 = build_list([2, 4, 3])  # represents 342
l2 = build_list([5, 6, 4])  # represents 465


solution = Solution()
result = solution.addTwoNumbers(l1, l2)

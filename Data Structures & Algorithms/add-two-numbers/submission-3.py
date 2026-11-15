# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry = 0
        while l1:
            l2Val = l2.val if l2 else 0
            total = l1.val + l2Val + carry
            if total >= 10:
                carry = 1
                total -= 10
            else: 
                carry = 0
            
            l1.val = total
            
            if not l1.next:
                if l2 and l2.next:
                    l1.next = l2.next
                    l2.next = None
                elif carry == 1:
                    l1.next = ListNode(1)
                    carry = 0

            l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        curr = head
        vals = []
        while curr:
            vals.append(curr.val)
            curr = curr.next
        print(vals)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
            
        dummy = ListNode()
        dummy.next = head

        prevEnd = dummy

        while True:
            curr = prevEnd

            for i in range(k):
                curr = curr.next
                if curr is None:
                    return dummy.next
            currEnd = curr

            prev = currEnd.next
            curr = prevEnd.next
            groupNext = currEnd.next
            
            while curr != groupNext:           
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            newCurrEnd = prevEnd.next
            prevEnd.next = currEnd

            prevEnd = newCurrEnd
            
                
            


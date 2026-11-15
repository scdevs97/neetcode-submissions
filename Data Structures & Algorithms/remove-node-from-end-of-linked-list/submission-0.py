# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if n == 0:
            return head
        
        dummy = ListNode()
        dummy.next = head

        curr = dummy
        listLength = 0
        while curr:
            curr = curr.next
            listLength += 1
        
        curr = dummy
        nodeNumToChange = listLength - n - 1
        for i in range(nodeNumToChange):
            curr = curr.next
        curr.next = curr.next.next
        
        return dummy.next
        
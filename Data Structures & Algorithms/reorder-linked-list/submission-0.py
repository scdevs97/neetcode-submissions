# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getListLength(self, head: ListNode) -> int:
        listLength = 0
        while head:
            head = head.next
            listLength += 1
        return listLength
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        # early return: if list is empty
        if not head:
            return

        # reverse later half of the list (1 > 2 > 3 > 4 becomes 1 > 2 > 3 < 4)
        listLength = self.getListLength(head)
        curr = head  
        for i in range(listLength // 2):
            curr = curr.next
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # maintains progressing pointer at both ends of the list, and alternates between both ends for the next node
        curr = left = head
        right = prev
        
        while curr:
            next = curr.next
            if curr == left:
                curr.next = right
                left = next
            else:
                curr.next = left
                right = next
            curr = curr.next





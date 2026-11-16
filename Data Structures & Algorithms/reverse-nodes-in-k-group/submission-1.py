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

    def reverseList(self, prevBlockEnd, currBlockStart, currBlockEnd):
        prev = currBlockEnd.next 
        curr = currBlockStart
        while curr != currBlockEnd:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        curr.next = prev
        if prevBlockEnd:
            prevBlockEnd.next = curr


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
            
        # get a block of k nodes, defined by its start and end node
        newHead = head

        prevBlockEnd = None
        currBlockStart = currBlockEnd = head

        while True:
            for i in range(k-1):
                currBlockEnd = currBlockEnd.next 
                # if less than k blocks remaining, return new head.
                if currBlockEnd is None:
                    return newHead
            
            # reverse the block
            self.reverseList(prevBlockEnd, currBlockStart, currBlockEnd)    
            # the end of the first block becomes the new head
            if newHead == head:
                newHead = currBlockEnd

            # set prevBlockEnd, currBlockStart, currBlockEnd for next iteration
            prevBlockEnd = currBlockStart
            currBlockStart = currBlockStart.next
            currBlockEnd = currBlockStart

            if currBlockStart is None:
                return newHead

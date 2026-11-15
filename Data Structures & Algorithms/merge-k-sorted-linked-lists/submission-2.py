# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        # look through the curr pointer of each list
        # pick the one with the smallest value (top of heap)
        # add that node to the return list and advance pointer for that one list
        curr = head
        sanitizedLists = []
        for l in lists:
            if not l:
                continue
            sanitizedLists.append(l)
        minHeap = [(l.val, i, l) for i, l in enumerate(sanitizedLists)]
        heapq.heapify(minHeap)

        while len(minHeap):
            minItem = heapq.heappop(minHeap)
            minIndex = minItem[1]
            minNode = minItem[2]
            curr.next = minNode
            if minNode.next:
                heapq.heappush(minHeap, (minNode.next.val, minIndex, minNode.next))
            curr = curr.next
        
        return head.next
        
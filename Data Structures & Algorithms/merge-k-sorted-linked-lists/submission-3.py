# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKListsHelper(self, lists, start, end):
        if start == end:
            return lists[start]

        middle = (start + end) // 2
        left = self.mergeKListsHelper(lists, start, middle)
        right = self.mergeKListsHelper(lists, middle + 1, end)

        head = ListNode()
        curr = head
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
            
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return head.next
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)
        
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        originalToClone = {}
        curr = head
        while curr:
            clone = Node(curr.val)
            originalToClone[curr] = clone
            curr = curr.next
        
        curr = head
        while curr:
            clone = originalToClone[curr]
            if curr.next:
                clone.next = originalToClone[curr.next]
            if curr.random:
                clone.random = originalToClone[curr.random]
            curr = curr.next
        return originalToClone[head]
        
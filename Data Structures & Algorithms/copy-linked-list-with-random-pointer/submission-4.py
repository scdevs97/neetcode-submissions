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
            if curr not in originalToClone:
                originalToClone[curr] = Node(0)
            if curr.next and curr.next not in originalToClone:
                originalToClone[curr.next] = Node(0)
            if curr.random and curr.random not in originalToClone:
                originalToClone[curr.random] = Node(0)
            
            originalToClone[curr].val = curr.val
            if curr.next:
                originalToClone[curr].next = originalToClone[curr.next]
            if curr.random:
                originalToClone[curr].random = originalToClone[curr.random]

            curr = curr.next

        return originalToClone[head]
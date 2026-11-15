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

        curr = head
        while curr:
            clone = Node(curr.val, None, curr.random)
            curr.random = clone
            curr = curr.next
        
        curr = head
        while curr:
            clone = curr.random
            clone.random = clone.random.random if clone.random else None
            clone.next = curr.next.random if curr.next else None
            curr = curr.next

        return head.random
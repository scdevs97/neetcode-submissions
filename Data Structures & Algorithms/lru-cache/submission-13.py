class ListNode:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize = capacity    
        self.cacheDict = {}
        
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.currSize = 0

    def removeFromHead(self): 
        nodeToRemove = self.head.next
        nodeToRemove.prev.next = nodeToRemove.next
        nodeToRemove.next.prev = self.head
        return nodeToRemove
            
    def setToTail(self, node: ListNode):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        if key in self.cacheDict:
            curr = self.cacheDict[key]
            self.setToTail(curr)
            return curr.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheDict:
            curr = self.cacheDict[key]
            curr.val = value
        else:
            curr = ListNode(key, value)
            if self.currSize == self.maxSize:
                nodeToRemove = self.removeFromHead()
                if nodeToRemove:
                    del self.cacheDict[nodeToRemove.key]
            else:
                self.currSize += 1
            self.cacheDict[key] = curr
                
        self.setToTail(curr)
        

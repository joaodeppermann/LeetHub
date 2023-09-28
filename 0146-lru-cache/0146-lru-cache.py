class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.front = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.front.prev = self.tail
        self.tail.next = self.front
    
    # Add a node to the front of the doubly linked list
    def add(self, node: ListNode):
        nxt, prev = self.front, self.front.prev
        node.next, node.prev = nxt, prev
        prev.next = nxt.prev = node
       
    # Remove a node from the doubly linked list
    def remove(self, node: ListNode):
        nxt, prev = node.next, node.prev
        nxt.prev = prev
        prev.next = nxt
        
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        # Get value
        ret = self.cache[key].val
        # Remove old node from list 
        self.remove(self.cache[key])
        # Delete old reference
        del self.cache[key]
        # Create new node and store reference to the node in cache
        self.cache[key] = ListNode(key, ret)
        # Add node to the front of the list
        self.add(self.cache[key])        
        return ret
        

    def put(self, key: int, value: int) -> None:
        # Check if the node already exists
        if key in self.cache:
            self.remove(self.cache[key])
            del[self.cache[key]]
        # Create a new node + reference and add it to the front
        # Create  for this node
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])
        # Remove from tail if needed
        if len(self.cache) > self.capacity:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
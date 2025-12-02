
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node) -> None:
        #insert right or append
        left,right = self.right.prev, self.right
        left.next, right.prev = node,node
        node.prev, node.next = left, right


    def remove(self, node) -> None:
        left, right = node.prev, node.next
        left.next = right
        right.prev = left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
 
    def put(self, key: int, value: int) -> None:

        #Update -> first remove node with old value and then add so that it becomes mru
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

        #remove lru if cap is crossed and Add New one
        if len(self.cache) >= self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])





        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
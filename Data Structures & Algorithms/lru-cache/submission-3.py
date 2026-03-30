class Node:
    def __init__(self, key: int = 0, val: int = 0, l: Optional[Node] = None, r: Optional[Node] = None):
        self.key = key
        self.val = val
        self.l = l
        self.r = r

class LRUCache:
    def __init__(self, capacity: int):
        self.lDummy = Node()
        self.rDummy = Node()
        self.lDummy.r = self.rDummy
        self.rDummy.l = self.lDummy

        self.hm = {}
        self.cap = capacity

    def remove(self, node: Node):
        node.l.r = node.r
        node.r.l = node.l

    def insert(self, node: Node):
        node.l = self.rDummy.l
        node.r = self.rDummy
        self.rDummy.l.r = node
        self.rDummy.l = node

    def get(self, key: int) -> int:
        if key not in self.hm: return -1

        node = self.hm[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.remove(self.hm[key])
            del self.hm[key]

        node = Node(key, value)
        self.hm[key] = node
        self.insert(node)

        if len(self.hm) > self.cap:
            lru = self.lDummy.r
            self.remove(lru)
            del self.hm[lru.key]
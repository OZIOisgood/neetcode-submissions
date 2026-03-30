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
        if not head: return None

        m = {None: None}

        # 1st pass
        cur = head
        while cur:
            m[cur] = Node(cur.val)
            cur = cur.next

        # 2nd pass
        cur = head
        while cur:
            node = m[cur]
            node.next   = m[cur.next]
            node.random = m[cur.random]
            cur = cur.next
        
        return m[head]
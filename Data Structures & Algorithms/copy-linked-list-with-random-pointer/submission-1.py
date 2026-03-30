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
        # Creating a hash map
        hm = {
            # With a default value of None translating as None
            # So there would be no problem with None pointer in the end of the list
            None: None,
        }

        # Starting from the beginning
        cur = head
        while cur:
            # Making a copy and adding it to the hash map
            hm[cur] = Node(cur.val)

            # Next
            cur = cur.next

        # Starting from the beginning
        cur = head
        while cur:
            # Getting a translation
            copy = hm[cur]
            
            # Changing a pointers for next and random
            copy.next = hm[cur.next]
            copy.random = hm[cur.random]

            # Next
            cur = cur.next
        
        # Result
        return hm[head]

        # Could be done in one pass
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node not in oldToNew:
                copy = Node(node.val)
                oldToNew[node] = copy
                for nei in node.neighbors:
                    newCopy = dfs(nei)
                    copy.neighbors.append(newCopy)
            return oldToNew[node]
        
        return dfs(node) if node else None
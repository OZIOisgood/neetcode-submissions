class PrefixTreeNode:

    def __init__(self):
        self.kids = {}
        self.isEnd = False
        
        
class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.kids:
                cur.kids[c] = PrefixTreeNode()
            cur = cur.kids[c]
        
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.kids:
                return False
            cur = cur.kids[c]
        
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.kids:
                return False
            cur = cur.kids[c]
        
        return True
        
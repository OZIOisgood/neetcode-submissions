class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                
            cur = cur.children[c]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.isEnd

            c = word[i]
            if c != '.':
                if c not in cur.children:
                    return False
                return dfs(i + 1, cur.children[c])
            else:
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                
                return False

        return dfs(0, self.root)
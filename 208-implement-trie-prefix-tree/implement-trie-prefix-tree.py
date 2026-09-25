#Solved the question but not implemented the required Trie
"""
class Trie:

    def __init__(self):
        self.words = {}
        self.wordsPrefix = set()
        

    def insert(self, word: str) -> None:
        self.words[word] = True
        for i in range(1,len(word)+1) :
            if word[:i] not in self.wordsPrefix :
                self.wordsPrefix.add(word[:i])
        

    def search(self, word: str) -> bool:
        if word in self.words:
            return True
        else :
            return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.wordsPrefix :
            return True
        else :
            return False
    
    """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word :
            if c not in cur.children :
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word :
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix :
            if c not in cur.children :
                return False
            cur = cur.children[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
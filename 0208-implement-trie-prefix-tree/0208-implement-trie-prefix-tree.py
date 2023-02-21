class Node:
    def __init__(self, data):
        self.children = {}
        self.isendofword = False
        self.val = data


class Trie:
    def __init__(self):
        self.root = Node("$")

    def insert(self, word: str) -> None: 
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = Node(c)
            ptr = ptr.children[c]
        # at the end of traversal, mark end of word flag 
        ptr.isendofword = True

    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.isendofword
            

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if not c in ptr.children:
                return False
            ptr = ptr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.isWordEnd = False
        self.children = {}
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def indexOfChar(self, c):
        return ord(c) - ord('a')

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for c in word:
            if not node.children.has_key(c):
                newNode = TrieNode()
                node.children[c] = newNode
                node = newNode
            else:
                node = node.children[c]
        node.isWordEnd = True
        

    def searchHelper(self, word):
        node = self.root
        for c in word:
            if not node.children.has_key(c):
                return None
            else:
                node = node.children[c]
        return node

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.searchHelper(word)
        if node:    return node.isWordEnd
        else:       return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.searchHelper(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

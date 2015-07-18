class TrieNode:
    # Initialize your data structure here.
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        while node:
            if word == node.value or node.value is None:
                node.value = word
                return
            elif word < node.value:
                if node.left is None:
                    node.left = TrieNode(value=word)
                    return
                else:
                    node = node.left
            elif word > node.value:
                if node.right is None:
                    node.right = TrieNode(value=word)
                    return
                else:
                    node = node.right
        

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        while node and node.value is not None:
            if word == node.value:
                return True
            elif word < node.value:
                node = node.left
            elif word > node.value:
                node = node.right
        return False
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        while node and node.value is not None:
            if prefix <= node.value:
                if node.value.startswith(prefix):
                    return True
                else:
                    node = node.left
            elif prefix > node.value:
                node = node.right
        return False
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

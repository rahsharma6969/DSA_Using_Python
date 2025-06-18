'''Approach
A Trie (or prefix tree) is a tree-like data structure that stores a dynamic set of strings, where the keys are usually strings. It is particularly useful for tasks like autocomplete, spell checking, and IP routing.
It consists of nodes, where each node represents a character in a string. The root node is empty, and each path from the root to a node represents a prefix of some strings stored in the Trie.'''

class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, value=None) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_end_of_word = True
        current.value = value

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def get_value(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value if current.is_end_of_word else None
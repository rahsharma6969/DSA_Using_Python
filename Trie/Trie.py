'''Trie Data Structure Implementation
This module implements a Trie (prefix tree) data structure.
A Trie (or prefix tree) is a tree-like data structure that stores a dynamic set of strings,
where the keys are usually strings. 
It is particularly useful for tasks like autocomplete, spell checking, and IP routing.
It consists of nodes, where each node represents a character in a string.
The root node is empty, and each path from the root to a node represents a prefix of some strings stored in the Trie.
'''

class Node:
    def __init__(self):
        self.children = {}   # Dictionary to hold child nodes
        self.is_end_of_word = False  # Boolean to indicate if the node marks the end of a word
        self.value = None  # Optional value associated with the word, can be used for additional data storage
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str, value=None) -> None:   # Insert a word into the Trie with an optional value
        current = self.root      
        for char in word:         
            if char not in current.children:
                current.children[char] = Node()   # initialize a new node if the character is not present
            current = current.children[char]   # Move to the child node
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
    
    
    
'''Explanation:
- The `Node` class represents a single node in the Trie, containing a dictionary of children nodes,
  a boolean to indicate if it is the end of a word, and an optional value.
  - The `Trie` class contains methods to insert words, search for words, 
  check for prefixes, and retrieve values associated with words.
- The `insert` method adds a word to the Trie, creating nodes as necessary.
- The `search` method checks if a word exists in the Trie.  
- The `starts_with` method checks if there is any word in the Trie that starts with a given prefix.
- The `get_value` method retrieves the value associated with a word if it exists.
- The Trie is efficient for prefix-based searches and can handle large datasets with many overlapping prefixes.
  '''
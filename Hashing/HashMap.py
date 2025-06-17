class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key):
        if not self.search(key):
            new_node = Node(key)
            new_node.next = self.head
            self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def get_all_keys(self):
        keys = []
        current = self.head
        while current:
            keys.append(current.key)
            current = current.next
        return keys

    def display(self):
        current = self.head
        while current:
            print(current.key, end=" -> ")
            current = current.next
        print("None")
    
    def remove(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


class HashTable:
    def __init__(self, size=5, load_factor_threshold=0.75):
        self.size = size 
        self.count = 0
        self.load_factor_threshold = load_factor_threshold
        self.table = [LinkedList() for _ in range(self.size)]

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def insert(self, key):
        if self.load_factor() > self.load_factor_threshold:
            self.resize()

        index = self.hash_function(key)
        if not self.table[index].search(key):  # Only increase count for new keys
            self.table[index].insert(key)
            self.count += 1

    def load_factor(self):
        return self.count / self.size
    
    def search(self, key):
        index = self.hash_function(key)
        return self.table[index].search(key)

    def resize(self):
        print(f"\n🔁 Resizing: Load factor {self.load_factor():.2f} > {self.load_factor_threshold}")
        old_table = self.table
        old_size = self.size
        self.size *= 2
        self.table = [LinkedList() for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key in bucket.get_all_keys():
                self.insert(key)

        print(f"✅ Resized from {old_size} to {self.size}")

    def display(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            self.table[i].display()

# Example usage
ht = HashTable()
words = ["apple", "banana", "grape", "cherry", "date", "fig", "elderberry", "guava"]

for word in words:
    ht.insert(word)

ht.display()

#Search for a key
key_to_search = "Rahul"
if ht.search(key_to_search):
    print(f"✅ '{key_to_search}' found in hash table.")
else:
    print(f"❌ '{key_to_search}' not found in hash table.")

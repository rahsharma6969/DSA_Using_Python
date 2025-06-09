class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None  # Top of the stack

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            raise IndexError("Stack is empty")
        value = self.head.value
        self.head = self.head.next
        return value

    def peek(self):
        if not self.head:
            raise IndexError("Stack is empty")
        return self.head.value

    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def is_full(self):
        # A linked list stack is never full unless memory is exhausted
        return False
    
    def get_size(self):
        if not self.head:
            return 0
        current = self.head
        size = 0
        while current.next:
            size += 1
            current = current.next
        return size
        

s  = StackLinkedList()
# s.push(1)
# s.push(2)
# s.push(3) 

print(s.get_size())
print(s.is_empty())
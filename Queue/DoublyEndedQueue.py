'''
Doubly Ended Queue (Deque) Implementation
This code implements a doubly ended queue (deque) using a linked list structure. It supports operations to add and remove elements from both ends of the queue.

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyEndedQueue:
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.size = 0
        
    def pushFront(self,val):
        node = Node(val)
        if self.size == 0:
            self.front = self.back = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        # `self.size += 1` is incrementing the size attribute of the doubly ended queue by 1. This is
        # done after successfully adding an element to the front of the queue using the `pushFront`
        # method. The size attribute keeps track of the number of elements currently in the queue.
        self.size += 1
        
    def pushBack(self, val):
        node = Node(val)
        if self.size == 0:
            self.front = self.back = node
        else :
            node.prev = self.back
            self.back.next = node
            self.back = node
        self.size += 1
        
    def popFront(self):
        if self.size == 0:
            return None
        value = self.front.value
        if self.size == 1:
            self.front = self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return value
    
    def popBack(self):
        if self.size == 0:
            return None
        value = self.back.value
        if self.size == 1:
            self.front = self.back = None
            
        else:
            self.back = self.back.prev
            self.back.next = None
            
        self.size -= 1
        return value
    
    def getfront(self):
        if self.size == 0:
            return None
        return self.front.value
    
    def getBack(self):
        if self.size == 0:
            return None
        return self.back.value
    
    def isEmpty(self):
        return self.size == 0
    
    def getsize(self):
        return self.size
    
    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements
    
    
# Example usage:
dll = DoublyEndedQueue()
dll.pushFront(10)
dll.pushBack(20)    
dll.pushFront(30)
dll.pushBack(40)
print(dll.getfront())  # Output: 30
print(dll.getBack())   # Output: 40
print(dll.display())  # Output: [30, 10, 20, 40]
    
        
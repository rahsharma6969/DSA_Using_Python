class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
        
    def enqueue(self, data):
        newNode = Node(data)
        if not self.front: 
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode 
            self.rear = newNode
        
    def dequeue(self):
        if not self.front:
            return "Queue is empty"
        removed_data= self.front.data
        self.front = self.front.next
        return removed_data
    
    def peek(self):
        if not self.front:
            return "Queue is empty"
        return self.front.data
    
    def back(self):
        if not self.rear:
            return "Queue is empty"
        
        return self.rear.data
    
    def is_Empty(self):
        return self.front is None
    
    def display(self):
        if not self.front:
            return "Queue is empty"
        current = self.front
        
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the queue
            
q = Queue()
q.enqueue(1)
q.enqueue(2)    
q.enqueue(3)
print("Queue after enqueuing 1, 2, 3:")
q.display()
q.dequeue()
print("\nQueue after dequeuing one element:")
q.display()
q.dequeue()
print("\nQueue after dequeuing another element:")
q.display()
q.enqueue(4)
print("\nQueue after enqueuing 4:")
q.display()

q.peek()
print("\nPeek at the front element:", q.peek())

q.back()
print("\nBack element of the queue:", q.back())
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Inserting at the head
    def prepend(self, data):
        new_node = Node(data)

        if not self.head:  # check if the list is empty
            new_node.next = self.head  # then we will directly append the new node to the head and tail
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  
            self.head = new_node
    
    # Inserting at the tail
    def append(self, data):
        new_node = Node(data)

        if not self.head:  # check if the list is empty
            new_node.next = self.head
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node 

    # delete the node
    def delete(self, target):

      if self.head is None:
        return "List is null"

    # Case 1: Target is at the head
      if self.head.data == target:
        to_delete = self.head
        self.head = self.head.next
        if to_delete == self.tail:  # In case head was also tail
            self.tail = None
        to_delete.next = None  # Clean up
        return

    # Case 2: Target is elsewhere
      prev = None
      nodetobedeleted = self.head

      while nodetobedeleted and nodetobedeleted.data != target:
        prev = nodetobedeleted
        nodetobedeleted = nodetobedeleted.next

      if nodetobedeleted is None:
        return "Node not found"

      prev.next = nodetobedeleted.next

      if nodetobedeleted == self.tail:
        self.tail = prev

      nodetobedeleted.next = None  # Clean up
    
    # insert at index
    def insertAtIndex(self, index, data):
        if index < 0:
            return "Invalid index"
            
        if index == 0: 
            self.prepend(data)
            return
        
        # find the index where we want to insert the new node
        current = self.head
        prev = None
        current_index = 0
        
        while current and current_index < index:
            prev = current
            current = current.next
            current_index += 1
        
        if current_index != index:
            return "Index out of bounds"
        
        new_node = Node(data)
        new_node.next = current.next
        
        if prev:
            prev.next = new_node
            
        else:
            self.head = new_node
        
        if new_node.next is None:
            self.tail = new_node
                 
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


L = LinkedList()
L.append(1)
L.append(2)
L.append(4)
L.append(5)

print(L.print(), "Linked List after inserting:")

L.insertAtIndex(2, 3)
print(L.print(), "Linked List after inserting at index 2:")
        

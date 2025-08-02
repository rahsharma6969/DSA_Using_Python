'''
82. Remove Duplicates from Sorted List II

Medium
Topics
premium lock icon
Companies
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
def deleteDuplicates(head):
    if not head:
        return None

    dummy = Node(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        # Detect duplicates
        if curr.next and curr.data == curr.next.data:
            dup_val = curr.data
            while curr and curr.data == dup_val:  
                curr = curr.next  
            prev.next = curr  # Skip all duplicates
        else:
            prev = curr
            curr = curr.next

    return dummy.next

            
                              
    

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
# Example usage
L = LinkedList()    
L.append(1)
L.append(2) 
L.append(3)
L.append(3)
L.append(4)
L.append(4)
L.append(5)
print("Original List:")
print_list(L.head)
L.head = deleteDuplicates(L.head)
print("List after removing duplicates:")
print_list(L.head)

    
'''

Code
Testcase
Test Result
Test Result
21. Merge Two Sorted Lists
Easy
Topics
premium lock icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]'''

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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
     
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")       
            
   
        
def mergeTwoLists(list1, list2):
    
    i = list1.head
    j = list2.head
    merged_list = LinkedList()
    while i and j:
        
        if i.data < j.data :            
            merged_list.append(i.data)            
            i = i.next
        
        else:
            merged_list.append(j.data) 
            j = j.next                    
    while i:
        merged_list.append(i.data)
        i = i.next
    while j:
        merged_list.append(j.data)
        j = j.next
    return merged_list



# Example usage
list1 = LinkedList()
list1.append(1)
list1.append(2) 
list1.append(4)
list2 = LinkedList()
list2.append(1)
list2.append(3)
list2.append(4)
merged_list = mergeTwoLists(list1, list2)
merged_list.print_list()  # Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
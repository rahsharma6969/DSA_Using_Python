'''
142. Linked List Cycle II
Medium
Topics
premium lock icon
Companies
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:


Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:


Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
 '''
 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class Solution:
    def dectectCycle(self, head):
        if not head:
            return None
        
        slow = head
        fast = head
        while fast and fast.next:  #  Ensure fast and fast.next are not None
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected, find the entry point
                entry = head
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return entry
        
    # Alternate approach using a set to detect cycle in a linked list

    def detectCycle(self, head):
        if not head:
            return None
        seen = set()
        
        current = head
        while current:
            if current in seen:
                return current
            seen.add(current)
            current = current.next
        return None
                
                
# Example usage:
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)  
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Creates a cycle
solution = Solution()
cycle_node = solution.detectCycle(head)       

print(f"Cycle starts at node with value: {cycle_node.val}" if cycle_node else "No cycle detected")
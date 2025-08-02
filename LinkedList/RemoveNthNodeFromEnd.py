'''
19. Remove Nth Node From End of List
Solved
Medium

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

# Definition for singly-linked list.

from typing import List , Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Two pass
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return None
        curr = head
        prev = ListNode(0, head)
        length = 0

        while curr:         
            length += 1
            curr = curr.next

        curr = prev
        for _ in range(length - n):
            curr = curr.next

        curr.next  = curr.next.next if curr else None

        return prev.next

# Single Pass        
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next

        # Delete the node
        slow.next = slow.next.next

        return dummy.next

            
        
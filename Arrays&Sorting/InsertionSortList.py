'''
147. Insertion Sort List

Medium
Topics

Companies
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0)  # Dummy node before the head of the sorted list
    curr = head

    while curr:
        prev = dummy
        next_temp = curr.next

        # Find the position to insert curr in the sorted part
        while prev.next and prev.next.val < curr.val:
            prev = prev.next

        # Insert curr between prev and prev.next
        curr.next = prev.next
        prev.next = curr

        # Move to the next node
        curr = next_temp

    return dummy.next

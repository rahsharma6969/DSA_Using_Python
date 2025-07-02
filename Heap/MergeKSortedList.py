'''
23. Merge k Sorted Lists
Solved
Hard
Topics
premium lock icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:
'''

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        counter = 0  # Tie-breaker for same val

        for l in lists:
            if l:
                # Add a tuple: (val, counter, node)
                heapq.heappush(min_heap, (l.val, counter, l))
                counter += 1

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, _, smallest_node = heapq.heappop(min_heap)
            current.next = smallest_node
            current = current.next

            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, counter, smallest_node.next))
                counter += 1

        return dummy.next

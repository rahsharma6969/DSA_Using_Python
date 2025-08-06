'''
Given an integer k and a queue of integers, we need to reverse the order of the first k elements of the queue, leaving the other elements in the same relative order.

Only following standard operations are allowed on queue.

enqueue(x) : Add an item x to rear of queue
dequeue() : Remove an item from front of queue
size() : Returns number of elements in queue.
front() : Finds front item.
Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.

"If the size of queue is smaller than the given k , then return the original queue."

Examples:

Input: q = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 4, 5]
Explanation: After reversing the first 3 elements from the given queue the resultant queue will be 3 2 1 4 5'''

class Solution:
    def reverseFirstK(self, q, k):
        #code here 
        if  k == -1 and k > len(q):
            return q
        stack = []
        
        for _ in range(k):
            stack.append(q.popleft())
            
        while stack:
            q.append(stack.pop())
            
        for _ in range(len(q) - k):
            q.append(q.popleft())
            
        return q
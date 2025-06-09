'''
Problem No: 225
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
'''

from collections import deque


class myStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.top_element = None
        self.size = 0
        
    def push(self, x: int):
        # Step 1: Push to q2
        self.q2.append(x)
        # Step 2: Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())  
        # Step 3: Swap names of q1 and q2
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        return self.q1.popleft() if not self.empty() else None
    
    def top(self):
        if not self.empty():
            self.top_element = self.q1[0]
            return self.top_element
        return None
    
    def empty(self):
        return len(self.q1) == 0
    
'''
Approach:
1. **Initialization**: Create two queues (`q1` and `q2`) to simulate the stack behavior. Use `top_element` to keep track of the last pushed element.
'''

# 2. **Push Operation**: When pushing an element:
#   - Add the element to `q2`.
#   - Move all elements from `q1` to `q2` to maintain the order.

# Usage:
#   - Swap the names of `q1` and `q2` so that `q1` always contains the stack elements in LIFO order.
    
# Example Usage:
stack = myStack()
stack.push(1)
stack.push(2)
# print(stack.top())  
print(stack.pop())  # Returns 2
print(stack.empty())  # Returns False
stack.push(3)
print(stack.top())  # Returns 3
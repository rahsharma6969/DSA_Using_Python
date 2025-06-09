'''
895. Maximum Frequency Stack
Solved
Hard
Topics
premium lock icon
Companies
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]
'''




from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)      # val -> frequency
        self.group = defaultdict(list)    # frequency -> stack of vals
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1      # Increment frequency of the value
        self.freq[val] = f          # Update the frequency map
        self.group[f].append(val)      # Add the value to the stack for this frequency

        if f > self.max_freq:      # Update the maximum frequency if necessary
            self.max_freq = f      

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()  # Most frequent, most recent
        self.freq[val] -= 1

        if not self.group[self.max_freq]:   # If no elements left at this frequency
            self.max_freq -= 1

        return val


'''
Approach:
1. Use a dictionary to keep track of the frequency of each element.
2. Use Another dictionary to keep track of the element with the highet freuency
3. Use a variable to keep track of the maximum frequency.add(element, frequency)
4. When popping, retrieve the most frequent element and update the frequency accordingly.
5. If the stack for the current maximum frequency is empty after popping, decrease the maximum frequency.

'''     


# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)     
obj.push(7)
obj.push(4)
obj.push(5)
print(obj.pop())

# param_2 = obj.pop()
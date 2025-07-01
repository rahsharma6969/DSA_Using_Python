'''
341. Flatten Nested List Iterator
Medium
Topics
premium lock icon
Companies
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

 

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].'''


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self._pushListToStack(nestedList)

    def _pushListToStack(self, nestedList):
        # Push elements in reverse order so we can pop from the end
        for item in reversed(nestedList):
            self.stack.append(item)
        
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
        
    
    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self._pushListToStack(top.getList())
        return False
         

'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.'''

class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       brack = { ")": "(", "]" : "[", "}" : "{" }   # dic to map closing bracket with their corresponding opening bracket

       for br in s: 
          if br in brack:   # checks when char is a closing bracket
            if stack[-1] == brack[br] and stack:  # checks if the stack is not empty and the top of the stack matches the corresponding opening bracket
                return True
            else:
                return False 
          else:
            stack.append(br)
       return not stack
            
'''
Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true'''

'''
Approach :
1. Initialize an empty stack to keep track of opening brackets.
2. Create a dictionary to map closing brackets to their corresponding opening brackets.
3. Iterate through each character in the string:
   - If the character is a closing bracket, check if the stack is not empty and if the top of the stack matches the corresponding opening bracket.
   - If it matches, pop the top of the stack; otherwise, return False.
   - If it's an opening bracket, push it onto the stack.
   '''
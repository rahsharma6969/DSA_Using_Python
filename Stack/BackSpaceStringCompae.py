'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 '''

def backspaceCompare(s, t):
    stack_s = []
    stack_t = []

    for i in s:
        if i == '#':
            if stack_s:
                stack_s.pop()
            else:
                stack_s.append(i)  # ✅ Only append if not '#'

    for j in t:
        if j == '#':
            if stack_t:
                stack_t.pop()
            else:
                stack_t.append(j)  # ✅ Only append if not '#'

    return stack_s == stack_t  # ✅ Compare actual contents
# Compare the final stacks
    
# Example usage:
s = "ab#c"
t = "ad#c"
result = backspaceCompare(s, t)
print(result)  # Output: True
'''
Approach:
1. Use two stacks to simulate the typing process for both strings.
2. For each character in the strings:
   - If it is a backspace ('#'), pop from the stack if it is not empty.
   - Otherwise, push the character onto the stack.
3. Finally, compare the two stacks to determine if the strings are equal after processing backspaces.

'''

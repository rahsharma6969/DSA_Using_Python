'''
1910. Remove All Occurrences of a Substring
Medium
Topics
premium lock icon
Companies
Hint
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
'''

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)

        for ch in s:
            stack.append(ch)
            # Check if the end of stack matches 'part'
            if len(stack) >= m and ''.join(stack[-m:]) == part:
                # Remove the last m characters
                for _ in range(m):
                    stack.pop()

        return ''.join(stack)
    
    
# Time complexity: O(n) where n is the length of the string s
# Space complexity: O(n) for the stack used to build the result string


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)  # remove only the first occurrence each time
        return s
# Time complexity: O(n * m) where n is the length of s and m is the length of part
# Space complexity: O(n) for the new string created by replace
            
        
        

'''
387. First Unique Character in a String
Solved
Easy
Topics
premium lock icon
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_char = {}

        for i in s:
          if i in freq_char:
            freq_char[i] += 1
          else:
            freq_char[i] = 1

        for j in s:
            if j in freq_char and freq_char[j] == 1:
                return s.index(j)
        return -1


        
        



        
        
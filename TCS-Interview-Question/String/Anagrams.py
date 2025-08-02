'''
242. Valid Anagram
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
'''

def isAnagram(s , t):
    if len(s) != len(t):
        return False
    
    mapping = {}
    
    for char in s:
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1
            
    for char in t:
        if char not in mapping or mapping[char] == 0:  # Check if char exists or has a count > 0
            return False            
        mapping[char] -= 1
    return True
        
    
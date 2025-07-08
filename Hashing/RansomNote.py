'''
383. Ransom Note
Easy
Topics
premium lock icon
Companies
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Approach 
 If every Element of ransomeNote is present in magazine then we can say it can be constructed otherwise No
'''

from typing import *
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(magazine)
        c2 = Counter(ransomNote)

        for char in c2 :
            if c1[char] < c2[char]:
                return False

        return True







        
        
'''
392. Is Subsequence
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false'''


def isSubsequence(s: str, t: str) -> bool:
    if not s or not t:
        return "" if not s else False
    
    i , j = 0,0
    
    while i< len(s ) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
        
    return i == len(s)
# Example usage:
if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))  # Output: True

    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s, t))  # Output: False
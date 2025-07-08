'''
290. Word Pattern
Easy
Topics
premium lock icon
Companies
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false

 '''
 
def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for char_p, word in zip(pattern, words):
        if char_p in char_to_word:
            if char_to_word[char_p] != word:
                return False
        else:
            char_to_word[char_p] = word

        if word in word_to_char:
            if word_to_char[word] != char_p:
                return False
        else:
            word_to_char[word] = char_p

    return True
            
            
        
        
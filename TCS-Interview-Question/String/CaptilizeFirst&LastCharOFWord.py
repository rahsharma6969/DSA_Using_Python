'''
Capitalize the first and last character of each word in a string
Last Updated : 07 Aug, 2022
Given the string, the task is to capitalise the first and last character of each word in a string.
Examples: 
 

Input: Geeks for geeks
Output: GeekS FoR GeekS

Input: Geeksforgeeks is best
Output: GeeksforgeekS IS BesT
'''

def capitalizeFirstAndLastCharOfWord(s):
    
    for char in s.split():  # As split function splits the string into words of a string and returns a list of words
        if len(char) > 1:
            # Capitalize the first and last character of the word
            char = char[0].upper() + char[1:-1] + char[-1].upper()
        else:
            # If the word is a single character, just capitalize it
            char = char.upper()
            
        print(char, end=' ')


# Example usage:
s = "geeks for geeks"
capitalizeFirstAndLastCharOfWord(s)
# Output: GeekS FoR GeekS


# Time Complexity : O(n), where n is the length of the string.
# Space Complexity : O(1), as we are not using any extra space except for the
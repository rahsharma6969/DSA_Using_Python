'''
Program to remove vowels from a String
Last Updated : 23 Jul, 2025
Given a string, remove the vowels from the string and print the string without vowels. 

Examples: 

Input : welcome to geeksforgeeks
Output : wlcm t gksfrgks

Input : what is your name ?
Output : wht s yr nm ?
'''

def removeVowels(s):
    
    vowels = "aeiouAEIOU"
    
    for char in s:
        if char not in vowels:
            print(char, end='')

# Time Complexity: O(n), where n is the length of the string.


    
    
            
# Example usage:
s = " what is your name "
removeVowels(s)
# Output: whtsyrnm
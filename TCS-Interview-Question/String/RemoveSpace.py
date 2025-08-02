# Remove spaces from a given string
# Last Updated : 06 Dec, 2024
# Given a string, remove all spaces from the string and return it. 

# Input:  "g  eeks   for ge  eeks  "
# Output: "geeksforgeeks"

# Input:  "abc d "
# Output: "abcd"



# Utility Function
def toString(List):
    return ''.join(List)

# Function to remove spaces
def removeSpaces(string):
    result = []

    # Traverse the given string
    for i in range(len(string)): 
        if string[i] != ' ':
            result.append(string[i])

    return toString(result)

# Driver program
string = "g  eeks  for ge  eeks  "
print(removeSpaces(string))

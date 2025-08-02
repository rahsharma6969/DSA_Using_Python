'''
'''

def first_non_repeating(arr):
    count = {}
    
    #Calculate frequency of each element
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    #Find the first non-repeating element
    for num in arr:
        if count[num] == 1:
            return num
    return None  # If no non-repeating element is found


# Example usage:
if __name__ == "__main__":
    arr = [4, 5, 1, 2, 0, 4]
    result = first_non_repeating(arr) 
    print("First non-repeating element:", result)  # Output: 5  
            
    
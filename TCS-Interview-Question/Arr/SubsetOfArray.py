'''
Check if an array is subset of another array
Last Updated : 31 Dec, 2024
Given two arrays a[] and b[] of size m and n respectively, the task is to determine whether
b[] is a subset of a[]. Both arrays are not sorted, and elements are distinct.

Examples: 

Input: a[] = [11, 1, 13, 21, 3, 7], b[] = [11, 3, 7, 1] 
Output: true

Input: a[]= [1, 2, 3, 4, 5, 6], b = [1, 2, 4] 
Output: true
'''
# using two pointer and sortng
def isSubset(a, b):
    # Convert both lists to sets for faster lookup    
    a.sort()
    b.sort()
    i , j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
            
        else:
           return False
    # If we have traversed all elements of b, it is a subset
    return j == len(b)  # means True
       


# using hashset

def IsSubset(a , b ):
    set_a = set(a)  # Convert list a to a set for O(1) lookups
   
    
    for element in b:
        if element not in set_a:
            return False
        else:
            continue
    return True  # means True
     
       
# driver code
if __name__ == "__main__":
  a = [1, 2, 3, 4, 5, 6]
  b =  [1, 2, 4] 

  if IsSubset(a, b):
      print("true")
  else:
      print("false")
            
            
    
    
            
            
    
    
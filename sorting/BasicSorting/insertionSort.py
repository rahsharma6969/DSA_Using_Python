''' 
Implementation of Insertion Sort

Working  : Here we do backward tracking 

PTR: We are not doing any kind of swap here.
We are just shifting an element

Time Complexity : O(  )
'''

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = element
    return arr  
   


# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertionSort(arr)         
    print("Sorted array is:", sorted_arr)  # Output: Sorted array is: [5, 6, 11, 12, 13]
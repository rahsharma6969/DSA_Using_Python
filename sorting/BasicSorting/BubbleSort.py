''' Bubble Sort Algorithm Implementation 
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    1. The algorithm repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
    2. The pass through the list is repeated until the list is sorted.  
    3. The algorithm gets its name from the way larger elements "bubble" to the top of the list.
    '''
    
    
#Using Iterative method   
def BubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        is_swapped = False
        for j in range(i+1, n):
            if arr[j] < arr[j+1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        # If no two elements were swapped by inner loop, then break
        if not is_swapped:
            break
    return arr


#using Recursion
def RecursiveBubbleSort(arr, n= None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[ i + 1]:
            arr[i] , arr[i + 1] = arr[i + 1], arr[i]
            
    RecursiveBubbleSort(arr, n - 1)
    return arr
    
        
        
        
        
        

if __name__ == "__main__":
    arr = [100, 234, 11, 34, 73, 13, 12, 22, 25, 64]
    sorted_arr = BubbleSort(arr)
    print("Sorted array:", sorted_arr)  # Output: Sorted array: [11, 12, 22, 25, 34, 64, 73, 100]
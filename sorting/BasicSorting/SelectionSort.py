''' Selection Sort Algorithm Implementation 
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    1.Their are two reiogns in the array, one is sorted and the other is unsorted.
    2.  We will select the minimum element from the unsorted region and swap it with the first element of the unsorted region.
    3.  We will repeat this process until the unsorted region is empty.
    '''
    

def SelectionSort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i  # To find the index of the minimum element in the unsorted region
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted region
        arr[i], arr[min_index] = arr[min_index], arr[i] 
    return arr

# Example usage:
if __name__ == "__main__":
    arr = [100,234,11,34,73,13,12,22,25,64]
    sorted_arr = SelectionSort(arr)
    print("Sorted array:", sorted_arr)  # Output: Sorted array: [11, 12, 22, 25, 64]
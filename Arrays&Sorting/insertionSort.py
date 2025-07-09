def insertionSort(arr):
    """
    Sorts an array using the insertion sort algorithm.

    Args:
        arr (_type_): _description_
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j= i-1
        
        while j>=0 and key < arr[j]:   # till the key is smaller than the previous element
            # Shift elements of arr[0..i-1], that are greater than key,
            arr[j+1] = arr[j]
            j -= 1  
        arr[j+1] = key  
    return arr


# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertionSort(arr)         
    print("Sorted array is:", sorted_arr)  # Output: Sorted array is: [5, 6, 11, 12, 13]
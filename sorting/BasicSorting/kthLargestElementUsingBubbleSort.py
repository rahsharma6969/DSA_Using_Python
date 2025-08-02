'''
Find the kth largest element in an array using Bubble Sort.
Time Complexity: O(n^2)'''


def kthLargestElementUsingPartialBubbleSort(arr, k):
    n = len(arr)

    for i in range(k):  # Only k passes needed
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Sort in ascending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # After k passes, the k largest elements are in the last k positions
    return arr[n - k]


if __name__ == "__main__":
    arr = [100, 234, 11, 34, 73, 13, 12, 22, 25, 64]
    k = 3
    kth_largest = kthLargestElementUsingPartialBubbleSort(arr, k)
    print(f"The {k}th largest element is: {kth_largest}")  # Output: The 3rd largest element is: 64
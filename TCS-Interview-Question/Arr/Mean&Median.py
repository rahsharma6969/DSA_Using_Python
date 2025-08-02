'''
Mean and Median of an Array
Last Updated : 27 Jun, 2025
Given an array arr[] of positive integers, find the Mean and Median, and return the floor of both values.

Note: Mean is the average of all elements in the array and Median is the middle value when the array is sorted, if the number of elements is even, it's the average of the two middle values.

Examples: 

Input: arr[] = [1, 2, 19, 28, 5]
Output: 11 5
Explanation: Sorted array - [1, 2, 5, 19, 28], Mean = (1 + 2 + 19 + 28 + 5) / 5 = 55 / 5 = 11, Median = Middle element = 5
'''

def findMedian(arr):
    n = len(arr)
    
    arr.sort()
    
    median = 0
    
    mid = n // 2
    
    if n % 2 == 0:
        median = (arr[mid - 1] + arr[mid]) // 2
        
    else:
        median = arr[mid]
        
    return median


def findMean(arr):
    total = sum(arr)
    n = len(arr)
    mean = total // n 
    return mean

def findMeanAndMedian(arr):
    
    mean = findMean(arr)
    median = findMedian(arr)
    return mean, median


if __name__ == "__main__":
    arr = [1, 2, 19, 28, 5]
    mean, median = findMeanAndMedian(arr)
    print(mean, median)  # Output: 11 5

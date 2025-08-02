'''
Program to print Sum of even and odd elements in an array
Given an array, write a program to find the sum of values of even and odd index positions separately.

Input : arr[] = {1, 2, 3, 4, 5, 6}
Output :Even index positions sum 9
        Odd index positions sum 12
        
Even = 1 + 3 + 5 = 9
Odd =  2 + 4 + 6 = 12

'''


def even_odd_sum(arr):
    even_sum , odd_sum = 0, 0
    for i in range(len(arr)):
        if i % 2 == 0:
            even_sum += arr[i]
        else:
            odd_sum += arr[i]
    return even_sum, odd_sum

'''Time Complexity: O(n)'''



# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    even_sum, odd_sum = even_odd_sum(arr)
    print("Even index positions sum:", even_sum)  # Output: 9
    print("Odd index positions sum:", odd_sum)    # Output: 12
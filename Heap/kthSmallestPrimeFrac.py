'''
786. K-th Smallest Prime Fraction
Solved
Medium
Topics
premium lock icon
Companies
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
'''
import heapq
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []

    # Step 1: Push (arr[0] / arr[j], 0, j) for all j > 0
        for j in range(1, n):
            heapq.heappush(heap, (arr[0] / arr[j], 0, j))

    # Step 2: Pop from heap k-1 times, and push next numerator in same column
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(heap)
            if i + 1 < j:  # move to the next numerator (still i < j)
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

    # Step 3: k-th smallest is now on top of heap
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
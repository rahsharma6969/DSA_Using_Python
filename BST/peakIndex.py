'''

Code
Testcase
Test Result
Test Result
852. Peak Index in a Mountain Array
Medium
Topics
premium lock icon
Companies
You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1
'''
from typing import List


from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        # endpoints can't be the peak in a valid mountain
        start, end = 1, n - 2

        while start <= end:
            mid = start + (end - start) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid  # found the peak
            elif arr[mid] < arr[mid + 1]:
                # we're on the increasing slope; move right
                start = mid + 1
            else:
                # we're on the decreasing slope; move left
                end = mid - 1

        # With valid mountain input, loop should return inside,
        # but if it exits, start will have converged to the peak.
        return start

    
if __name__ == "__main__":
    s = Solution()
    print(s.peakIndexInMountainArray([0,1,0]))
    print(s.peakIndexInMountainArray([0,2,1,0]))
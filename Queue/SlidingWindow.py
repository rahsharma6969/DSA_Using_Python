'''
239. Sliding Window Maximum
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]'''

from collections import deque
class Solution:
  def maxSlidingWindow(self,nums, k):
    if not nums or k == 0:
        return []

    deq = deque()
    result = []

    for i in range(len(nums)):
        # Remove indices out of the current window
        if deq and deq[0] <= i - k:
            deq.popleft()

        # Remove indices whose values are less than nums[i]
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        # Add current index to deque
        deq.append(i)

        # Append max value to result list once first window is complete
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


'''
Approach:
1. **Initialization**: Create a deque to store indices of the elements in the current window and a list to store the maximums.
2. **Iterate through the array**: For each element in the array:
   - Remove indices from the front of the deque that are out of the bounds of the current window.
   - Remove indices from the back of the deque while the current element is greater than the elements at those indices (this ensures that we always have the maximum at the front).
   - Append the current index to the deque.
   - If we have filled at least one window (i.e., `i >= k - 1`), append the maximum (the element at the index stored at the front of the deque) to the result list.
   Time Complexity: O(n), where n is the number of elements in the input array. Each element is added and removed from the deque at most once.
Space Complexity: O(k), where k is the size of the sliding window, as we store indices in the deque.'''
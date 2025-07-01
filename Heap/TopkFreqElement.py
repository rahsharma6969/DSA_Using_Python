'''
347. Top K Frequent Elements
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''


import heapq
from collections import Counter
from typing import List

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap= []
        freq_map = Counter(nums)

        for num , freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return  [num for freq, num in min_heap]
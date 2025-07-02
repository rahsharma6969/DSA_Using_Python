'''

973. K Closest Points to Origin
Solved
Medium
Topics
premium lock icon
Companies
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]'''


import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        

        for x,y in points:
            dist_sq = x*x + y*y
            heapq.heappush(max_heap ,(-dist_sq,x,y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[x, y] for (_, x, y) in max_heap]
    
    import heapq

def kClosest(points, k):
    min_heap = []

    for x, y in points:
        dist = x**2 + y**2
        heapq.heappush(min_heap, (dist, x, y))  # store (distance, point)

    result = []
    for _ in range(k):
        _, x, y = heapq.heappop(min_heap)
        result.append([x, y])

    return result

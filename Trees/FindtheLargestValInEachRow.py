from collections import deque
from typing import List, Optional

'''
515. Find Largest Value in Each Tree Row
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
'''


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        queue = deque([root])
        result = []
        
        while queue:
            level_size = len(queue)
            level_node = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_node.append(node.val)
                
                if node.left:
                   queue.append(node.left)
                   
                if node.right:
                    queue.append(node.right)
                    
            result.append(max(level_node))
        return result  
            
'''
Approach:
Use Level Order Traversal to traverse the tree level by level
and find the max value in each level.
Time Complexity:
O(n), where n is the number of nodes in the tree.
Space Complexity:
O(m), where m is the maximum number of nodes at any level in the tree.
'''


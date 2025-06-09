'''
993. Cousins in Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
'''

from __future__ import annotations
from collections import deque
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def isCousins(self, root: 'TreeNode', x: int, y: int) -> bool:
        if not root:
            return False
        
        queue = deque([root])
        found_x = found_y = False
        depth_x = depth_y = -1
        depth = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.val == x:
                    found_x = True
                    depth_x = depth
                elif node.val == y:
                    found_y = True
                    depth_y = depth
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if found_x and found_y:
                break
            
            depth += 1
        
        return found_x and found_y and depth_x == depth_y
    

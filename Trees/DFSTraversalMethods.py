'''94. Binary Tree Inorder Traversal
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the inorder traversal of its nodes' values.'''

from collections import deque
 
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorderTraversal(self, root):
        if not root:
            return []
        result =[]
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)

        return result 
     
    def preorderTraversal(self, root): 
        if not root:
            return []
    
        result = []
        result.append(root.val)  # Step 1: Visit root
        result += self.preorderTraversal(root.left)   # Step 2: Traverse left
        result += self.preorderTraversal(root.right)  # Step 3: Traverse right
    
        return result
'''Prbolem Statement:
Given the root of a binary tree, invert the tree, and return its root.
This means that for every node in the tree, you swap its left and right children.

# 226. Invert Binary Tree

'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def invertTree(self, root):
    
      if not root:
        return None

      queue = deque([root])

      while queue:
        current = queue.popleft()

        # Swap children
        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

      return root
    
    def InversionUsingRecurrsion(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.InversionUsingRecurrsion(root.left)
        self.InversionUsingRecurrsion(root.right)
        return root

#Time Complexity: O(n)
'''
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0
            
            left_height = check_balance(node.left)
            if left_height == -1:   # If left subtree is not balanced, propagate -1 up
                return -1
            
            right_height = check_balance(node.right)
            if right_height == -1:    # If right subtree is not balanced, propagate -1 up
                return -1
            
            if abs(left_height - right_height) > 1:   # If the current node is not balanced
                return -1
            
            return max(left_height, right_height) + 1
        
        return check_balance(root) != -1
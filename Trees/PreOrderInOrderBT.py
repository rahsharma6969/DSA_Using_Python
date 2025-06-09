'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium
Topics
premium lock icon
Companies
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
'''

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        # Find the index of the root in inorder
        root_index = inorder.index(root_val)
        # Elements to the left of root_index in inorder are part of the left subtree
        left_inorder =inorder[:root_index]
        # Elements to the right of root_index in inorder are part of the right subtree
        right_inorder = inorder[root_index+1:]
        # Elements in preorder after the root are divided into left and right subtrees
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]
        # Recursively build the left and right subtrees
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        # Return the constructed tree
        return root
        
        
        
        
       
        
        return root
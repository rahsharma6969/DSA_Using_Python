'''
700. Search in a Binary Search Tree
Easy
Topics
premium lock icon
Companies
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self,root, val:int ) -> TreeNode:
        """_summary_

        Args:
            root (_type_): _description_
            val (int): _description_

        Returns:
            TreeNode: _description_
        """
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right, val)
        
        
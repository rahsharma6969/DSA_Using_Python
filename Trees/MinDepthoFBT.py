'''
111. Minimum Depth of Binary Tree
Easy
Topics
premium lock icon
Companies
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5'''

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1+ self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    
# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    min_depth = solution.minDepth(root)

    print(min_depth)  # Output: 2, as the minimum depth is the path 3 -> 9.        
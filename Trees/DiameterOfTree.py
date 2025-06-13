'''

Code
Testcase
Test Result
Test Result
543. Diameter of Binary Tree
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


'''


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Update the diameter if the path through this node is longer
            self.diameter = max(self.diameter, left_depth + right_depth)
            # Return the depth of the node
            return max(left_depth, right_depth) + 1
        
        depth(root)
        return self.diameter

    def HeighOfBinaryTree(self, root):
        if not root:
            return 0
        lef_height = self.HeighOfBinaryTree(root.left)
        right_height = self.HeighOfBinaryTree(root.right)
        return max(lef_height, right_height) + 1



''' Approach:
1. Define a TreeNode class to represent each node in the binary tree.
2. Define a Solution class with methods to calculate the diameter and height of the binary tree.
3. The diameter is calculated by finding the maximum path length between any two nodes, which is the sum of the heights of the left and right subtrees for each node.
4. The height of the tree is calculated recursively by finding the maximum height of the left and right subtrees.'''
c = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
c.diameterOfBinaryTree(root)
print("Diameter of Tree", c.diameter)  # Output: 3, the diameter is the path 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3
print("Height of Tree:", c.HeighOfBinaryTree(root))  # Output: 3, the height of the tree is 3

'''337. House Robber III
Solved
Medium
Topics
premium lock icon
Companies
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.'''


class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return (0, 0)  # (rob, not_rob)
            
            left = helper(node.left)
            right = helper(node.right)

            # If we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]

            # If we don't rob this node, we can rob its children or not
            not_rob = max(left) + max(right)

            return (rob, not_rob)
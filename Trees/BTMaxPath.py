'''
124. Binary Tree Maximum Path Sum
Solved
Hard
Topics
premium lock icon
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
'''

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')  # global max path sum

        def dfs(node):
            if not node:
                return 0

            # Recursively get the max gain from left and right, ignoring negative paths
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            # Path that passes through this node (could be a split path)
            current_path_sum = node.val + left_gain + right_gain

            # Update global max if this is better
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the max one-sided path to parent
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_sum

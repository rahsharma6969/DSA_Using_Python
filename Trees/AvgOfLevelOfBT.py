'''

Code
Testcase
Test Result
Test Result
637. Average of Levels in Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return the average value of the nodes on each 
level in the form of an array. Answers within 10-5 of the actual answer will be accepted.'''

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result
    
# Example usage:
# Create a binary tree:      3
#                        /   \
#                       9     20    
#                          /  \
#                         15   7    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
avg_levels = root.averageOfLevels(root)
print(avg_levels)  # Output: [3.0, 14.5, 11.0]
    
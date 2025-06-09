'''

Code
Testcase
Test Result
Test Result
513. Find Bottom Left Tree Value
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''

from collections import deque
from typing import Optional
from test.test_concurrent_futures.test_deadlock import _return_instance

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None  
        queue = deque([root])
        left_most = root.val
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == 0:
                    left_most = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return left_most

# Example usage:
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
solution = Solution()
print(solution.findBottomLeftValue(root))  # Output: 1
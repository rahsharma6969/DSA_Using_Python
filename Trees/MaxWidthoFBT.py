'''
662. Maximum Width of Binary Tree
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # (node, index)
        while queue:
            level_length = len(queue)
            # Retrieve the index of the first node at the current level
            _, first_index = queue[0]
            for i in range(level_length):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            # The width of the current level is the index of the last node minus the index of the first node plus one
            _, last_index = queue[-1] if queue else (None, index)
            max_width = max(max_width, last_index - first_index + 1)
        # Return the maximum width found
        return max_width
    
# Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
# Space Complexity: O(n), for the queue that stores nodes at each level.
# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    solution = Solution()
    max_width = solution.widthOfBinaryTree(root)

    print(max_width)  # Output: 4, as the maximum width is at the level of nodes 4, 5, and 6.
    
    '''
    
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
'''
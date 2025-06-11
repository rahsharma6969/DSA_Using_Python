'''
652. Find Duplicate Subtrees
Medium
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.   How to solve it'''

from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        def serialize(node):
            if not node:
                return "#"
            serial = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            count[serial] += 1
            if count[serial] == 2:
                duplicates.append(node)
            return serial
        count = defaultdict(int)
        duplicates = []
        serialize(root)
        return duplicates
    
# Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
# Space Complexity: O(n), for the storage of serialized strings in the dictionary and the list of duplicates.   
# Example usage:
if __name__ == "__main__":
    # Create a binary tree with duplicate subtrees
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(4)
    root.right.right = TreeNode(4)

    solution = Solution()
    duplicates = solution.findDuplicateSubtrees(root)

    # Print the values of the duplicate subtrees
    for dup in duplicates:
        print(dup.val)  # Output: 4, 2
        

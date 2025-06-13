'''
230. Kth Smallest Element in a BST
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        result = []
        def in_order_traversal(node):
            if not node:
                return
            in_order_traversal(node.left)
            result.append(node.val)
            in_order_traversal(node.right)
        in_order_traversal(root)
        return result[k-1] 
# Example usage:
if __name__ == "__main__":
    # Create a binary search tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(8)

    k = 3

    solution = Solution()
    kth_smallest_value = solution.kthSmallest(root, k)

    print(kth_smallest_value)  # Output: 4, as the 3rd smallest value in the BST is 4.
        
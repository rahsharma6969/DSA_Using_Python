'''Prbolem Statement:
Given the root of a binary tree, invert the tree, and return its root.
This means that for every node in the tree, you swap its left and right children.

# 226. Invert Binary Tree

'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def invertTree(self, root):
    
      if not root:
        return None

      queue = deque([root])

      while queue:
        current = queue.popleft()

        # Swap children
        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

      return root
    
    def InversionUsingRecurrsion(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.InversionUsingRecurrsion(root.left)
        self.InversionUsingRecurrsion(root.right)
        return root

#Time Complexity: O(n)
#Space Complexity: O(n) for the queue in the iterative approach, O(h) for the recursion stack in the recursive approach, where n is the number of nodes and h is the height of the tree.
# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    # Invert the binary tree using iterative method
    inverted_tree_iterative = root.invertTree(root)

    # Invert the binary tree using recursive method
    inverted_tree_recursive = root.InversionUsingRecurrsion(root)
    
    # The structure of the inverted tree can be checked by printing or debugging
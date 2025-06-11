'''
951. Flip Equivalent Binary Trees
Medium
Topics
premium lock icon
Companies
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
      if not root1 and not root2:
          return True
      if not root1 or not root2:
          return False
      if root1.val != root2.val:
          return False

      if (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)): #if two trees are same without flip
          return True
      if (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)): # if two trees are same with flip
          return True
      return False


# Time Complexity: O(n), where n is the number of nodes in the trees, since we visit each node once.
# Space Complexity: O(h), where h is the height of the trees, due to the recursion stack.
#Example usage:
if __name__ == "__main__":
    # Create two binary trees
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(5)
    root2.right.right = TreeNode(4)

    solution = Solution()
    result = solution.flipEquiv(root1, root2)

    print(result)  # Output: True, as the two trees are flip equivalent.
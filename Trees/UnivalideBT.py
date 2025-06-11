'''
965. Univalued Binary Tree
Easy
Topics
premium lock icon
Companies
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

'''

from collections import defaultdict

def isUnivalTree(root):
    if not root:
        return True
    def check_value(root, value):
        if not root:
            return True
        if root.val != value:
            return False
        return check_value(root.left, value) and check_value(root.right, value)
    return check_value(root, root.val)
### without recursion
from collections import deque

def isUnivalTree(root):
    if not root:
        return True
    
    value = root.val
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node.val != value:
            return False
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return True


# Time Complexity: O(n), where n is the number of nodes in the tree, since we visit each node once.
# Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.    
# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    print(isUnivalTree(root))  # Output: True
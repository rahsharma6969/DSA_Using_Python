'''
450. Delete Node in a BST
Medium
Topics
premium lock icon
Companies
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.'''

 """
        Deletes a node with the given key from the BST.
        
        Args:
            root (TreeNode): The root node of the BST.
            key (int): The value of the node to be deleted.
        
        Returns:
            TreeNode: The root node of the BST after deletion.
        """
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self.getMin(root.right)
            root.val = min_larger_node.val  # Copy the inorder successor's value to this node
            root.right = self.deleteNode(root.right, min_larger_node.val)  # Delete the inorder successor
        
        return root
    
    def getMin(self, node: TreeNode) -> TreeNode:
        """Helper function to find the minimum value node in a subtree."""
        while node.left:
            node = node.left
        return node
    
# Cases
'''
1. Node with no children (leaf node).
2. Node with one child (either left or right).  
3.Node with two children (both left and right).
4. Node to be deleted is the root node.'''
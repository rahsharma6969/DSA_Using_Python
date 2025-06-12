'''
701. Insert into a Binary Search Tree
Medium
Topics
premium lock icon
Companies
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
Example 1:
Input: root = [4,2,7,1,3], val = 5  
Output: [4,2,7,1,3,5]'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertInToBST(self, root:TreeNode, val:int) -> TreeNode:
        """
        Inserts a new value into a Binary Search Tree (BST).
        Args:
            root (TreeNode): The root node of the BST.
            val (int): The value to insert into the BST.
        Returns:
            TreeNode: The root node of the BST after insertion.
        If the root is None, a new TreeNode with the given value is created and returned.
        Otherwise, the function recursively finds the correct position for the new value
        according to BST properties and inserts it.
        """
        if not root:    # If the root is None, create a new TreeNode with the given value
            return TreeNode(val)   
        
        if val < root.val:
           root.left = self.insertInToBST(root.left,val)
           
        else:   
           root.right = self.insertInToBST(root.right,val)  
          
        return root
    
# Example usage:
if __name__ == "__main__":
    # Create a binary search tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    val_to_insert = 5

    solution = Solution()
    new_root = solution.insertInToBST(root, val_to_insert)

    # Function to print the tree in-order for verification
    def in_order_traversal(node):
        if not node:
            return []
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

    print(in_order_traversal(new_root))  # Output: [1, 2, 3, 4, 5, 7]
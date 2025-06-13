'''
606. Construct String from Binary Tree
Medium
Topics
premium lock icon
Companies
Given the root node of a binary tree, your task is to create a string representation of the tree following a specific set of formatting rules. The representation should be based on a preorder traversal of the binary tree and must adhere to the following guidelines:

Node Representation: Each node in the tree should be represented by its integer value.

Parentheses for Children: If a node has at least one child (either left or right), its children should be represented inside parentheses. Specifically:

If a node has a left child, the value of the left child should be enclosed in parentheses immediately following the node's value.
If a node has a right child, the value of the right child should also be enclosed in parentheses. The parentheses for the right child should follow those of the left child.
Omitting Empty Parentheses: Any empty parentheses pairs (i.e., ()) should be omitted from the final string representation of the tree, with one specific exception: when a node has a right child but no left child. In such cases, you must include an empty pair of parentheses to indicate the absence of the left child. This ensures that the one-to-one mapping between the string representation and the original binary tree structure is maintained.

In summary, empty parentheses pairs should be omitted when a node has only a left child or no children. However, when a node has a right child but no left child, an empty pair of parentheses must precede the representation of the right child to reflect the tree's structure accurately.

Example 1:
Input: root = [1,2,3,4] 
Output: "1(2(4))(3)"'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        """
        Constructs a string representation of a binary tree in preorder traversal format.
        
        Args:
            root (TreeNode): The root node of the binary tree.
        
        Returns:
            str: The string representation of the binary tree.
        """
        if not root:
            return ""
        
        # Start with the current node's value
        result = str(root.val)
        
        # If there is a left child, add its string representation
        
        if root.left or root.right:                 # Include left child if it exists or if there is a right child
            result += f"({self.tree2str(root.left)})"
        
        # If there is a right child, add its string representation
        if root.right:  # Always include right child if it exists
            result += f"({self.tree2str(root.right)})"
            
        # Return the constructed string
        
        return result
    
# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)

    solution = Solution()
    tree_string = solution.tree2str(root)

    print(tree_string)  # Output: "1(2(4))(3)"
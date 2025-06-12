'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is
defined between two nodes p and q as the lowest
node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Finds the lowest common ancestor (LCA) of two nodes in a binary tree.
    Args:
        root (TreeNode): The root node of the binary tree.
        p (TreeNode): The first node for which to find the LCA.
        q (TreeNode): The second node for which to find the LCA.
    Returns:
        TreeNode: The lowest common ancestor of nodes p and q. Returns None if either node is not present in the tree.
    Approach:
        - Recursively traverse the tree.
        - If the current node is either p or q, return the current node.
        - Search for p and q in the left and right subtrees.
        - If both left and right recursive calls return non-None values, the current node is the LCA.
        - Otherwise, return the non-None result from the left or right subtree.
    """
    def lowestCommonAncestor(self,root,p: TreeNode,q:TreeNode) ->TreeNode:
       
        if not root:
            return None
        
        if root == p or root == q: # If the current node is either p or q, we have found one of the nodes
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q) # Search in the left subtree
        right = self.lowestCommonAncestor(root.right,p,q) # Search in the right subtree
        
        if left and right:  # If both left and right are not None, it means p and q are found in different subtrees
            return root
        return left if left else right  # If one of them is None, return the other (which could be None or the found node)
    
# Example usage:
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left  # Node with value 5
    q = root.left.right.right  # Node with value 4

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)

    print(lca.val)  # Output: 5, as it is the LCA of nodes 5 and 4
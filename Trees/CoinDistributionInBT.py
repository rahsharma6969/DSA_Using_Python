'''
979. Distribute Coins in Binary Tree
Solved
Medium
Topics
premium lock icon
Companies
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root 
[taking two moves]. Then, we move one coin from the root of the tree to the right child.'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root):
        moves = 0

        def dfs(node):
            nonlocal moves
            if not node:
                return 0

            # Get balances from left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Moves = total coins moved from/to this node
            moves += abs(left) + abs(right)

            # Return current node’s balance:
            # (coins at this node + left balance + right balance - 1 coin to keep)
            return node.val + left + right - 1

        dfs(root)
        return moves


#Example
if __name__ == "__main__":
    # Example usage:
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(0)

    solution = Solution()
    print(solution.distributeCoins(root))  # Output: 2
    
#Internal Working of the above code:
# The function `distributeCoins` calculates the minimum number of moves required to distribute coins in a binary tree.
# It uses a depth-first search (DFS) approach to traverse the tree and compute the balance of coins at each node.
# The `dfs` function returns the balance of coins for each node, while also updating the total number of moves required to 
# achieve the desired distribution. The final result is returned as the total number of moves needed.
# The code is efficient and works in O(n) time complexity, 
# where n is the number of nodes in the tree, as it visits each node exactly once.

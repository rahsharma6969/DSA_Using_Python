'''
Write a Left Rotation function for AVL Tree'''


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.height = 1
        
class AVLTree:
    
    def __init__(self):
        self.root = None
        
    def Insert(self, root, key):
        # Perform normal BST insert
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.Insert(root.left, key)
        else:
            root.right = self.Insert(root.right, key)

        # Update height of this ancestor node
        root.height = 1 + max(self.Height(root.left), self.Height(root.right))

        # Get the balance factor
        balance = self.GetBalance(root)

        # If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.RightRotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.LeftRotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root)

        return root
        
    
    def Height(self, node):
        if not node:
            return 0
        return node.height
    
    def RightRotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        # Update heights
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))
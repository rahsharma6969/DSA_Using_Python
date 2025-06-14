'''
109. Convert Sorted List to Binary Search Tree
Medium
Topics
premium lock icon
Companies
Given the head of a singly linked list where elements 
are sorted in ascending order, convert it to a height-balanced binary search tree.'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def SortedListToBST(self, head:ListNode) -> TreeNode:
        if not head:
            return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def BuildTree(left,right):
            if left > right:
                return None
            mid = (left+right) // 2
            node = TreeNode(arr[mid]) 
            node.left = BuildTree(left,mid - 1)
            node.right = BuildTree(mid + 1, right)
            return node
        return BuildTree(0, len(arr) - 1)
    
    # def sortedListToBST(self,head):
    # # Step 1: Get length of linked list
    # def getLength(node):
    #     length = 0
    #     while node:
    #         length += 1
    #         node = node.next
    #     return length

    # length = getLength(head)
    # current = [head]  # wrap in list to make it mutable in nested scope

    # # Step 2: Recursively build BST
    # def buildBST(left, right):
    #     if left > right:
    #         return None
        
    #     mid = (left + right) // 2

    #     # Recursively build left subtree
    #     left_child = buildBST(left, mid - 1)

    #     # Current list node is root
    #     root = TreeNode(current[0].val)
    #     root.left = left_child

    #     # Move to next list node
    #     current[0] = current[0].next

    #     # Recursively build right subtree
    #     root.right = buildBST(mid + 1, right)

    #     return root

    # return buildBST(0, length - 1)
    
    ''' Approach:
    1. Convert the linked list to an array to facilitate easy access to elements.
    2. Use a recursive function to build the BST:
    - Find the middle element of the current subarray to ensure balance.    
    - Create a TreeNode with the middle element.
    - Recursively build the left subtree with the left half of the array.
    - Recursively build the right subtree with the right half of the array.'''
        
        '''
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the linked list once to convert it into an array and then build the BST from the array.
Space Complexity: O(n), where n is the number of nodes in the linked list. We store the values in an array before constructing the BST.
        '''
        
        
        
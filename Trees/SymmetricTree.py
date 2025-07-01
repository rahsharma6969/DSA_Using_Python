'''
101. Symmetric Tree
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''

def isSymmetric(root):
    
    if not root:
        return True
    
    def isMirror(t1,t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        
        return(
            t1.val == t2.val and
            isMirror(t1.left, t2.right) and
            isMirror(t1.right, t2.left)
        )
        
    return isMirror(root.left, root.right )


from collections import deque

def IsSymmetric(root):
    if not root:
        return True

    queue = deque()
    queue.append((root.left, root.right))

    while queue:
        t1, t2 = queue.popleft()

        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False

        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))

    return True
        

            
        
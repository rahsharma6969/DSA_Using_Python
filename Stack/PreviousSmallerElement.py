'''
Previous Smaller Element '''

def previousSmallerElements(arr):
    stack = []
    res = []

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()
        
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        
        stack.append(num)

    return res

# Example
arr = [4, 5, 2, 10, 8]
print(previousSmallerElements(arr))  # Output: [-1, 4, -1, 2, 2]

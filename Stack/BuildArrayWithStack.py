def buildArray(target, n):
    stack = []
    current = 1
    for i in target:
        while current < i:
            stack.append("Push")
            stack.append("Pop")
            current += 1
          
        stack.append("Push")      
        current += 1 
    return stack






#Example usage:
target = [2, 3,4]   
n = 3
print(buildArray(target, n))  

'''Approach: The function iterates through the target array and simulates the stack operations.
It pushes elements onto the stack until it reaches the current target element, 
popping elements as necessary to skip over any numbers not in the target.'''
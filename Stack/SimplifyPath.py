'''You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

 '''

from turtle import st


def SimplifyPath(path):
       stack = []
       new_path = path.split("/")

       for char in new_path:
         if char == "" or char == ".":
            continue
         elif char == "..":
            if stack:
                stack.pop()
         else:
            stack.append(char)
             
       return "/" + "/".join(stack)
    
    
path = "/../"
simplified_path = SimplifyPath(path)
print(simplified_path)  # Output: "/c"


'''# Time Complexity: O(n), where n is the length of the input path.
# Space Complexity: O(n), where n is the number of directories in the simplified path.
'''

'''
Approach
1. Split the input path by the '/' character to get individual components.
2. Initialize an empty stack to keep track of the directories.
3. Iterate through each component:
   - If the component is empty or a single period '.', skip it.
   - If the component is a double period '..', pop the last directory from the stack if it exists.
   - Otherwise, push the component onto the stack.
   '''
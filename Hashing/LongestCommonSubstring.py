'''3. Longest Substring Without Repeating Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 '''
 
def length_of_longest_substring(s: str) -> int:
    max_length = 0
    current = ""

    for char in s:
        if char in current:
            index = current.index(char)
            current = current[index + 1:]
        current += char
        max_length = max(max_length , len(current))

    return max_length

#Example usage
if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(f"Input: {s1}, Output: {length_of_longest_substring(s1)}")  # Output: 3
    print(f"Input: {s2}, Output: {length_of_longest_substring(s2)}")  # Output: 1
    print(f"Input: {s3}, Output: {length_of_longest_substring(s3)}")  # Output: 3
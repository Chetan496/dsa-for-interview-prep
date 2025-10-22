"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.

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

Technique: Sliding Window
"""

def length_of_longest_substring(s):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "dvdf"]
    
    for s in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: '{s}' -> Output: {result}")

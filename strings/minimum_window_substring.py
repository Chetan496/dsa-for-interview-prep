"""
Problem: Minimum Window Substring
Difficulty: Hard

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such window, return the empty string "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.

Technique: Sliding Window + Hash Map
"""

def min_window(s, t):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("ab", "b"),
        ("abc", "cba")
    ]
    
    for s, t in test_cases:
        result = min_window(s, t)
        print(f"Input: s = '{s}', t = '{t}' -> Output: '{result}'")

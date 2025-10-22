"""
Problem: Valid Palindrome
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.

Technique: Two Pointers
"""

def is_palindrome(s):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "Madam",
        "No 'x' in Nixon"
    ]
    
    for s in test_cases:
        result = is_palindrome(s)
        print(f"Input: '{s}' -> Output: {result}")

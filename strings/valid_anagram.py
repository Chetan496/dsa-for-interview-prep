"""
Problem: Valid Anagram
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Technique: Hash Map or Sorting
"""

def is_anagram(s, t):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("listen", "silent"),
        ("hello", "bello"),
        ("", "")
    ]
    
    for s, t in test_cases:
        result = is_anagram(s, t)
        print(f"Input: s = '{s}', t = '{t}' -> Output: {result}")

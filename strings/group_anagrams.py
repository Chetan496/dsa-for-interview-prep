"""
Problem: Group Anagrams
Difficulty: Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Technique: Hash Map + Sorting
"""

def group_anagrams(strs):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "xyz", "zyx", "yxz"]
    ]
    
    for strs in test_cases:
        result = group_anagrams(strs)
        print(f"Input: {strs} -> Output: {result}")

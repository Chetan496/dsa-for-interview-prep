"""
Problem: Product of Array Except Self
Difficulty: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Technique: Prefix/Suffix Products
"""

def product_except_self(nums):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [2, 3, 4, 5],
        [1, 0]
    ]
    
    for nums in test_cases:
        result = product_except_self(nums)
        print(f"Input: {nums} -> Output: {result}")

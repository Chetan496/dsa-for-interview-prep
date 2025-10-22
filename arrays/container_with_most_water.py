"""
Problem: Container With Most Water
Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container that can contain the most water.
Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Technique: Two Pointers
"""

def max_area(height):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [4, 3, 2, 1, 4],
        [1, 2, 1]
    ]
    
    for height in test_cases:
        result = max_area(height)
        print(f"Input: {height} -> Output: {result}")

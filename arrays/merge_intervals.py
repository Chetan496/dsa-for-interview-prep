"""
Problem: Merge Intervals
Difficulty: Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Technique: Sorting + Greedy
"""

def merge(intervals):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        [[1, 4], [2, 3]],
        [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    ]
    
    for intervals in test_cases:
        result = merge(intervals)
        print(f"Input: {intervals} -> Output: {result}")

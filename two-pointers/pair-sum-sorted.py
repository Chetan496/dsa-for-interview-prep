# Given an array of integers numbers that is already sorted in non-decreasing order, write a function to find two numbers in the array that add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an array of size 2.
# Constraints:

# The array is 1-indexed (meaning the first element is at index 1, not 0)
# Each input has exactly one solution
# The same element cannot be used twice
# Input array is already sorted in ascending order
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]

# Input: numbers = [-1,0], target = -1
# Output: [1,2]

from typing import List


class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
      l = 0 #left ptr
      r = len(numbers) - 1 #right ptr

      while l < r:
         if numbers[l] + numbers[r] > target:
            r = r - 1
         if numbers[l] + numbers[r] < target:
            l = l + 1 
         if numbers[l] + numbers[r] == target:
            return [l,r]        
      return []
      
  
if __name__ == "__main__":
    solution = Solution()
    list = [-5,-2,3,4,6]  
    target = 7
    pair = solution.twoSum(list, target)
    print(len(pair))
    if len(pair) > 0:
       print("The two numbers whose sum is {} are at index {} and {}. These numbers are {} and {}".format(target, pair[0], pair[1], list[pair[0]], list[pair[1]]) )
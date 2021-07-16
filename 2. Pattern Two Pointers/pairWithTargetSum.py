import pytest

def findPair(sortedArray, targetSum):
    left = 0
    right = len(sortedArray) - 1
    pair = []
    while left < len(sortedArray):       
        while left < right:
            currSum = sortedArray[left] + sortedArray[right]
            if currSum == targetSum:
                pair.append(sortedArray[left])
                pair.append(sortedArray[right])
                return pair
            elif currSum > targetSum:
                right = right - 1
            elif currSum < targetSum:
                break
        left = left + 1

        
def test_findPair_test1():
    assert findPair([2,3,5,9,11], 11) == [2,9]


def test_findPair_test2():    
    assert findPair([2,3,5,9,11], 12) == [3,9]

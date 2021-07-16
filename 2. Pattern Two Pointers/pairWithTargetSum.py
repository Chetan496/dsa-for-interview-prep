import pytest

def findPair(sortedArray, targetSum):
    left = 0
    right = len(sortedArray) - 1
    pair = []
    while left < right:
        currSum = sortedArray[left] + sortedArray[right]
        if currSum == targetSum:
            pair.append(sortedArray[left])
            pair.append(sortedArray[right])
            return pair
        elif currSum > targetSum:
            right = right - 1
        else:
            left = left + 1


        
def test_findPair_test1():
    assert findPair([2,3,5,9,11], 11) == [2,9]


def test_findPair_test2():    
    assert findPair([2,3,5,9,11], 12) == [3,9]

    
def test_findPair_test3():    
    assert findPair([2,3,5,10,11], 15) == [5,10]

def maxFruitsInTwoBaskets(inputArray):
    startIdx = 0
    windowSize = 1
    max = 0
    while startIdx < len(inputArray):
      while (startIdx + windowSize) <= len(inputArray):
        uniqueFruits = countOfUniqueFruitsInSubArray(inputArray, startIdx, windowSize)
        if uniqueFruits == 2:
            fruitsCount = windowSize 
            if fruitsCount > max:
                max = fruitsCount
        windowSize += 1
        
      startIdx += 1
      windowSize = 1
      
    return max    

        
def countOfUniqueFruitsInSubArray(inputArray, startIdx, windowSize):
    fruitSet = set()
    i = startIdx
    endIdx = startIdx + windowSize
    while i < endIdx:
        fruitSet.add(inputArray[i])
        i += 1
    return len(fruitSet)

def main():
    inputArray = ['A', 'B', 'C', 'A', 'C']
    result = maxFruitsInTwoBaskets(inputArray)
    print(result)

if __name__ == "__main__":
    main()

'''
Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

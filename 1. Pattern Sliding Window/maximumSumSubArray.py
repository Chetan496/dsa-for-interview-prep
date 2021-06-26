def maxSumOfSubArray(input_list, windowSize):
    startIdx = 0
    maxSum = 0
    while startIdx < len(input_list):
        if startIdx + windowSize > len(input_list):
            break
        currentSum = subArraySum(input_list, startIdx, windowSize)
        if currentSum > maxSum:
            maxSum = currentSum
        startIdx = startIdx + 1
    return maxSum
            

def subArraySum(input_list, startIdx, windowSize):
    i = startIdx
    endIdx = startIdx + windowSize
    sum = 0
    while i < endIdx:
        sum = sum + input_list[i]
        i = i + 1
    return sum

def main():
    inputArray = [2,3,4,1,5]
    k = 2
    maxSum = maxSumOfSubArray(inputArray,k)
    print(maxSum)

if __name__ == "__main__":
    main()

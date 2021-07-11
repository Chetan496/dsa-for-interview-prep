def squaresOfSortedArray(sorted_array):
    i = 0;
    firstArray=[]
    secondArray=[]
    while(i<len(sorted_array)):
        square = sorted_array[i] * sorted_array[i]
        if sorted_array[i] < 0:
            firstArray.append(square)
        else:
            secondArray.append(square) 
        i = i + 1

    idx1 = len(firstArray) - 1
    idx2 = 0

    mergedArray=[]
    while idx1 >= 0 and idx2 < len(secondArray):
        if (firstArray[idx1] < secondArray[idx2] ):
           mergedArray.append(firstArray[idx1])
           idx1 = idx1 - 1
        else:
           mergedArray.append(secondArray[idx2])
           idx2 = idx2 + 1

    if idx1 < 0:
        #just append items from secondArray to mergedArray
        while idx2 < len(secondArray):
            mergedArray.append(secondArray[idx2])
            idx2 = idx2 + 1
    else:
        #append items from firstArray to mergedArray in reverse order
        while idx1 >= 0:
            mergedArray.append(firstArray[idx1])
            idx1 = idx1 - 1

    return mergedArray
        


def main():
    sorted_array = [-2,-1,0,2,3]
    result=squaresOfSortedArray(sorted_array)
    print(result)


# -2 -1 0 2 3
# square all elements 
# remember index of 0 
# idx = 2
# 4 1 0 4 9 
# you now have to merge subarray [0..1] with subarray [2..4]
# so merge of [4 1] needs to be done with [0 4 9]
# the first array is guaranteed to be in descending order because the original numbers were negative
# create a third array which has length of: len(array1) + len(array2)
# do a merge sort but in reverse way and add items in third array

    
# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]
    

if __name__ == "__main__":
    main()    

def smallestSubArray(input_list, sum):
    list_size = len(input_list)
    window_size = 0
    while window_size < list_size:
        start_idx = 0
        while start_idx < list_size:
            if start_idx + window_size > list_size:
                break;
            print("calling sumForSubArray with startIdx %d and window_size %d"% (start_idx, window_size))
            subArraySum = sumForSubArray(input_list, start_idx, window_size)
            print("subArraySum: %d"% (subArraySum))
            if subArraySum >= sum:
                return window_size
            start_idx = start_idx + 1
        window_size = window_size + 1
        
    return 0
            

def sumForSubArray(input_list, start_idx, window_size):
    sum = 0
    i = start_idx
    j = start_idx + window_size
    while i < j:
        sum = sum + input_list[i]
        i = i + 1
    return sum
        
        
def main():
    input_list = [2,1,5,2,8]
    result = smallestSubArray(input_list, 7)
    print(result)
    

if __name__ == "__main__":
    main()    

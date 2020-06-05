def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # instantiate a low variable (the beginning of the lists indices)
    low = 0
    # instantiate a high variable (the end of the lists indices)
    high = len(arr)-1
    # a while loop 
    while low <= high: 
        # instantiate a middle variable (between low and high)
        middle = (low+high)//2
        # if the the target is smaller than the middle
        if target < arr[middle]:
            # the middle is assigned to high - 1 elimainating the RHS
            high = middle-1 # -1 elimainate current middle
            # if the target is larger than the middle
        elif target > arr[middle]:
            # the middle is assigned to low + 1 elimainating the LHS
            low = middle+1 # +1 elimainate current middle
        else:
            # else middle is the target
            return middle


    return -1  # not found

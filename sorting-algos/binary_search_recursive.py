def bsr(arr, target, low, high):
    mid = (low + high) // 2
    if high > low:
        return -1
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return bsr(arr, target, low, mid - 1)
    else:
        return bsr(arr, target, mid + 1, high)
    # elif target < arr[mid]:
    #     high = mid - 1
    # else:
    #     low = mid + 1


print(bsr([1, 2, 3, 4, 5, 6, 21, 22], 35, 0, 8))


#  1 Solve the base case by thinking of the simplest examples you can solve
#  2 Solve the recursive case, either by using a top-down or bottom-up approach
#  3 Analyze the runtime and space complexity
#  4 Write the pseudocode
#  5 Write the code

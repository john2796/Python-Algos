def bsr(arr, target, low, high):
    print(arr)
    mid = (low + high) // 2
    if low > high:
        return -1
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return bsr(arr, target, low, mid - 1)
    else:
        return bsr(arr, target, mid + 1, high)


test = [1, 2, 3, 12, 5, 6, 21, 22]
print(bsr(test, 12, 0, len(test) - 1))


#  1 Solve the base case by thinking of the simplest examples you can solve
#  2 Solve the recursive case, either by using a top-down or bottom-up approach
#  3 Analyze the runtime and space complexity
#  4 Write the pseudocode
#  5 Write the code

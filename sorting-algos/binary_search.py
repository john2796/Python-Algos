def binary_search(arr, target):
    # has to be sorted arr
    low = 0
    high = len(arr) - 1
    # need mid divide and conquer
    # case 1  base case stop when target is found
    # case 2: target (2) < mid (3) = true ? remove right
    # case 3 if false remove left by moving midpoint else remove left
    while low <= high:  # 0 <= length of arr
        mid = (low + high) // 2
        print(arr[low: high], target, "<", arr[mid])
        if target == arr[mid]:
            return True
        elif target < arr[mid]:  # remove right if True
            high = mid - 1
        else:  # remove left if False
            low = mid + 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 21, 22,
                     23, 24, 25, 26, 31, 32, 33, 34, 35, 36], 35))

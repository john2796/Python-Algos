def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0

    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    print(arrA, "< ", arrB, "result : ", merged_arr,
          '<------------------------compare and merge')
    return merged_arr


# recursive sorting function ---> O (log n)
def merge_sort(arr):
    print(arr, '<------------------------split')
    if len(arr) > 1:
        mid = int(len(arr) // 2)
        left = merge_sort(arr[0: mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)   # merge() defined later
    return arr


arr = [3, 2, 1, 4, 5, 6]
print(arr, merge_sort(arr))

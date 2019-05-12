

# def merge(left, right):
#     elems = len(left) + len(right)
#     x = [0] * elems
#     l = 0
#     r = 0
#     for i in range(0, elems):
#         # case for empty left and right
#         if l >= len(left):
#             x[i] = right[r]
#             r += 1
#         elif r >= len(right):
#             x[i] = left[l]
#             l += 1
#         # case for l < r then store to x
#         elif left[l] < right[r]:
#             x[i] = left[l]
#             l += 1
#         else:
#             x[i] = right[r]
#             r += 1
#         print(left, right, left[l],  right[r],  x, i)
#         return x


# def merge_sort(a):
#     if len(a) > 1:
#         mid = len(a) / 2
#         l = merge_sort(a[0:mid])
#         r = merge_sort(a[:mid])
#         return merge(l, r)


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0

    for i in range(0, elements):
        # print(arrA, arrB, merged_arr, '<------------------------l&r')
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
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr) // 2)
        left = merge_sort(arr[0: mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)   # merge() defined later
    print(arr, '<------------------------l&r')
    return arr


arr = [3, 2, 1, 4, 5, 6]
print(arr, merge_sort(arr))

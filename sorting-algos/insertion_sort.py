arr = [55, 2, 3, 4, 5, 22, 31]


def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        print(arr)
    return arr
# [55, 2, 3, 4, 5, 22, 31]
# [2, 55, 3, 4, 5, 22, 31]
# [2, 3, 55, 4, 5, 22, 31]
# [2, 3, 4, 55, 5, 22, 31]
# [2, 3, 4, 5, 55, 22, 31]
# [2, 3, 4, 5, 22, 55, 31]
# [2, 3, 4, 5, 22, 31, 55]
# [2, 3, 4, 5, 22, 31, 55]


print(insertion_sort(arr))

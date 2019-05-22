arr = [3, 1, 5, 4, 2]


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


print(insertion_sort(arr))

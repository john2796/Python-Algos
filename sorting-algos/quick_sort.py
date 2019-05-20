

arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]
# iterative solution

# print(swapp(arr, 0, len(arr) - 1))


def quick_sort(arr, low, high):
    if low <= high:
        pi = partition(arr, low, high)
        print(pi, 'testing')
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    pass


def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    print(arr, 'before', i)
    for j in range(low, high):
        print(arr, "counter i:", i, "counter j:", j, arr[j], "<=", pivot)
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return (i + 1)


# print(quick_sort(arr, 0, len(arr) - 1))
print(quick_sort(arr, 0, len(arr) - 1))

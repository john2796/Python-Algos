

arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]
# iterative solution

#print(swapp(arr, 0, len(arr) - 1))


def quick_sort(arr):
    pass


def partition(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(0, len(high) - 1):
        print(j)


def swapp(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
    return arr


print(quick_sort(arr))
print(partition(arr, 0, len(arr)))

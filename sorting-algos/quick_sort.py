

arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]
# iterative solution

#print(swapp(arr, 0, len(arr) - 1))


def quick_sort(arr):
    pivot = arr[0]
    c1 = 1
    c2 = 2
    print(arr, 'prev', c1, c2)
    if c2 < pivot:
        swapp(arr, c1, c2)
        c1 += 1
        c2 += 1
    else:
        c1 += 1
        c2 += 1
    print(arr, c1, c2)
    pass


def swapp(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
    return arr


print(quick_sort(arr))

#findPivot(arr, 0, len(arr) - 1)

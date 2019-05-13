
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    if l > r:
        print(arr)
        return
    else:
        m = int(len(arr) // 2)
        merge_sort_in_place(arr, arr[0:m], r)
        merge_sort_in_place(arr, l, arr[:m])
        merge_in_place(arr, l, m,  r)
    pass


arr = [3, 2, 1, 4, 5, 6]
print(arr, merge_sort_in_place(arr, 0, len(arr) - 1))

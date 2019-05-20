arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]


def insertion_sort(arr):
    unsorted_len = len(arr)
    # need to run until unsorted length is 0
    while unsorted_len > 0:
        sorted_arr = [arr[0]]
        unsorted_arr = arr[1:]
        print(sorted_arr, unsorted_arr)
        for j in range(0, len(unsorted_arr)):
            if unsorted_arr[0] < sorted_arr[0]:
                temp = unsorted_arr[0]
                unsorted_arr[0] = sorted_arr[0]
                sorted_arr[0] = temp
            else:
                sorted_arr.append(unsorted_arr[0])

        # need a sorted array
        # need an unsorted arr
        # compare items in sorted array and first item in unsertorted array
        # if unsorted is smaller then swap it in the sorted array to go to it's proper position
        break
    pass


print(insertion_sort(arr))

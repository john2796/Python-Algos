arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]


def bubble_sort(arr):
    i = 0
    size = len(arr)
    print(size)
    # keep running until length of arr is 0 which means all of the item is in the right pos
    while size > 0:
        for j in range(1, size):
            print(size, i, j, arr)
            # compare j < i  ?
            if arr[j] < arr[i]:
               # if yes and swap i and j
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
          # increment pointers
            i += 1
            j += 1
        print('hit ------------------')
        # once length of arr is completed
        # subtract 1 to the last item because it should be the correct pos and reset i = 0
        i = 0
        size -= 1

        print(size, i, j, arr)
    return arr


bubble_sort(arr)

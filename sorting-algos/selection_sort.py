arr = [5, 2, 1, 4, 3]


def selection_sort(arr):
  # Traverse through all array elements
    for i in range(len(arr)):
        print(arr)
        min_idx = i
        # Find the minimum element in remaining
        # unsorted array
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp

    return arr


print(selection_sort(arr))

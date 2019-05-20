

arr = [17, 41, 5, 22, 54, 6, 29, 3, 13]
# iterative solution

# print(swapp(arr, 0, len(arr) - 1))


def quick_sort(arr, low, high):
    if low <= high:
      # partition function every call of the function will execute
        pi = partition(arr, low, high)
        # left side of arr smaler
        quick_sort(arr, low, pi - 1)
        # right side of arr larger
        quick_sort(arr, pi + 1, high)
        print(
            f"partition:{pi} --->, low:{low},---> high:{high}, ---->  arr:{arr}")
    pass


def partition(arr, low, high):
  # grab last item as pivot
    pivot = arr[high]
    # starts at negative 1
    i = (low - 1)
    print(arr, 'before', i)
    # loop through starting to end
    for j in range(low, high):
        # if j counter is less than or equal pivot swap
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    # swap i + 1 to last item
    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp
    return (i + 1)


# print(quick_sort(arr, 0, len(arr) - 1))
print(quick_sort(arr, 0, len(arr) - 1))

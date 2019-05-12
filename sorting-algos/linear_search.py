def linear_search(arr, target):
    idx = 0
    # compare first index to next index see if it's even
    # then increment idx
    print(len(arr), '--------------------------------->')
    while idx <= len(arr):  # 0 <
        print(arr, '<-------------->', idx)
        if target == arr[idx]:
            return True
        else:
            idx += 1


# O(n)
print(linear_search([1, 2, 3, 4, 5, 6, 21, 22,
                     23, 24, 25, 26, 31, 32, 33, 34, 35, 36], 25))

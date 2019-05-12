def binary_search(arr, target):
    # has to be sorted arr
    l = 0
    r = len(arr) - 1
    mid = (l + r) // 2
    print(mid)
    # need mid divide and conquer
    # case 1  base case stop when target is found
    # case 2: target (2) < mid (3) = true ? remove right
    # case 3  else remove left
    # while len(arr) < 0:
    #     mid = (l + r) // 2
    #     if arr[mid] == target:
    #         return target
    #     elif target < arr[mid]:
    #         arr = arr[l: mid]
    #     else:
    #         arr = arr[mid: r]
    #     return target


print(binary_search([1, 2, 3, 4, 5, 6], 2))

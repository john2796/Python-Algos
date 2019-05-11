

def merge(left, right):
    elems = len(left) + len(right)
    x = [0] * elems
    l = 0
    r = 0
    for i in range(0, elems):
        print(left, right, left[l],  right[r]  x, i)
        # case for empty left and right
        if l >= len(left):
            x[i] = right[r]
            r += 1
        elif r >= len(right):
            x[i] = left[l]
            l += 1
        # case for l < r then store to x
        elif left[l] < right[r]:
            x[i] = left[l]
            l += 1
        else:
            x[i] = right[r]
            r += 1


print(merge([6, 2, 1], [5, 4, 7]))

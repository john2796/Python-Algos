# 1. Donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'

# and donuts(23) returns 'Number of donuts: many'


def donuts(count):
    # Your code here
    if count <= 10:
        print('hit 1')
        return f'Number of donuts: {count}'
    else:
        print('hit 2')
        return f'Number of donuts: many'


print(donuts(5))

# 2. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.


def both_ends(s):
    # Your code here
    return s[:2] + s[-2:]


print(both_ends('spring'))

# 3. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    # Your code here
    # have all the occurence "*" example 'babble' -> 'ba**le'

    q = [char for char in s]
    visited = {}
    res = ""
    while len(q) > 0:
        v = q.pop(0)
        print(v, 'v <-- ')
        if v not in visited:
            visited[v] = 1
            res += v
        else:
            res += "*"
    print(visited)
    return res


print(fix_start('fckkkg awesome Yee'), 'fix_start <--')

# 4. mix_up
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b, str):
    # Your code here
    # loop through str
    for idx in range(0, len(str)):
        print(str[idx], '<--', idx)
    # find a and b then swap
    return str


print(mix_up("m", "p", "mix pod"))

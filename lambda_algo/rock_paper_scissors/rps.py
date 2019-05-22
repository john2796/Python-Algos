#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # list with all of the possible Rock Paper Scissors plays.
    rps_posibility = ['rock', 'paper', 'scissors']
    #  * Another problem that asks you to generate a bunch of permutations, so we're probably going to want to opt for using recursion again. Since we're building up a list of results, we'll have to pass the list we're constructing around to multiple recursive calls so that each recursive call can add to the overall result. However, the tests only give our function `n` as input. To get around this, we could define an inner recursive helper function that will perform the recursion for us, while allowing us to preserve the outer function's function signature.
    #  * In Python, you can concatenate two lists with the `+` operator. However, you'll want to make sure that both operands are lists!
    #  * If you opt to define an inner recursive helper function, don't forget to make an initial call to the recursive helper function to kick off the recursion.
    for i in range(0, n):
        for y in rps_posibility:
            print(y, '---> ', i)
            rps_posibility[i] = [y]
    return rps_posibility
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')


# `n`,  represents the number of plays per round.
# rock_paper_scissors(0)  # [[]]
print(rock_paper_scissors(1))  # [['rock'], ['paper'], ['scissors']]
# rock_paper_scissors(2)
# [['rock', 'rock'],   ['rock', 'paper'], ['rock', 'scissors'],
#  ['paper', 'rock'],  ['paper', 'paper'], ['paper', 'scissors'],
# ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

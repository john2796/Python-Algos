#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # expecting how recipe can be made with ingredients
    max_number_batches = 0
    first_step = False
# loop through ingredients object
    for i in ingredients:
        if recipe.__contains__(i) and len(recipe) == len(ingredients):
            print(i)
        else:
            return 0
    # check each of value of ingredients and divide them to get how many recipe can be made
        recipe_count = recipe[i]
        ing_count = ingredients[i]
        result = ing_count // recipe_count
    # if everything is greater than 1 then store it else we just return 0
    # print(result)
    # 1 2 10        2  >  1
        if result == 0:
            return 0
        elif first_step and result > max_number_batches:
            print(max_number_batches)
        elif result > max_number_batches:
            first_step = True
            max_number_batches = result

    return max_number_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


print('tsdt')

# Condition 1: Always produces the same output with arguments
# Condition 2: No side effects (No print statement/Touching no other variable)


from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))

# Functions- map, filter, zip, reduce (To think in terms of functional programming)

# 1. map()


def multiply_by3(item):
    return item*3


print(list(map(multiply_by3, [1, 2, 3])))

# 2. filter()


def only_odd(item):
    return item % 2 != 0  # False


print(list(filter(only_odd, [1, 2,  3])))

# 3. zip() - zip 2 iterables together

my_list = ['sally', 'jon', 'sam']  # Could be tuples too
your_list = [10, 20, 30]  # Can be used to map 2 lists from .csv

print(list(zip(my_list, your_list)))  # [(1, 10), (2, 20), (3, 30)]

# 4. reduce() -


a_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item  # This value is then the value of 'acc' in next iteration


print(reduce(accumulator, a_list, 0))  # 0 is the inital value of 'acc'

# lambda Expressions - One time anonymous functions that need to run only ONCE

# Syntax- lambda param: action(param)
print(list(map(lambda item: item*2, a_list)))
print(list(filter(lambda item: item % 2 != 0, a_list)))
print(reduce(lambda acc, item: acc+item, a_list))

lam_list = [5, 4, 3]

# Use lambda to square number

print(list(map(lambda item: item ** 2, lam_list)))


# List Sorting- Sort according to second value in tuple
a = [(0, 2), (4, 3), (10, -1), (9, 9)]

# A way to adjust sorting; also works with dictionaries
a.sort(key=lambda item: item[1])
print(a)

# Comprehensions
comp_list = [char for char in 'hello']
print(comp_list)  # Prints ['h','e','l','l','o']

comp_list2 = [num for num in range(0, 100)]
print(comp_list2)  # Prints list [0, 1....,100]

comp_list3 = [num*2 for num in range(0, 100)]
print(comp_list3)  # Prints list [0, 2....,200]

comp_list4 = [num*2 for num in range(0, 100) if num % 2 == 0]
print(comp_list4)  # Prints list [0, 2....,200]

simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)

if True:
    print('hello')
elif True:  # Elif
    print('sup')
else:
    print('Hola')


age = 18
legal = 21
# Ternary Operator
result = print("OK") if age == 18 else print("Go Home")

# For loop
user = {
    'name': 'Golem',
    'age': 55,
    'can_swim': False
}

for item in user.items():  # or user.values(), or user.keys()
    print(item)  # Prints all key-value pairs in tuples

for k, v in user.items():
    print(k, v)  # Prints key, value but not in tuple


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for item in my_list:
    sum = sum + item

print(sum)

#  When variable is not necessary, replace with _
for _ in range(0, 10, 2):
    print('Will print 0 through 10 with increment of 2')

for _ in range(2):
    print(list(range(10)))  # prints array [0,1,2...,10] twice

# Exercise - Print a tree
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')  # Overrides \n in the end of print
        else:
            print(' ', end='')
    print('')  # By default, does \n
print(picture)

l = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# How to print duplicate values in list
# list_list = list(set(l))
duplicates = []
for value in l:
    if l.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


def hello(name, emoji):
    print(f'Hello {name}{emoji}')


hello('Saugaat', 'emoji1')

# *args, **kwargs
# Rule: params, *args, default parameters, **kwargs


# def super_func(*args, **kwargs):
#     print(*args)
#     return sum(args)


# super_func(1, 2, 3, 4, 5, num1=1, num2=10)

# Global variables
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())  # Prints 3

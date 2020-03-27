print(2 + 4)
print(type(2 + 4))  # int
print(type(2 / 4))  # float
print(type(9.9 + 1.1))  # float
print(2 ** 3)  # 2^3 = 8
print(14 // 3)  # 14/3 quotient = 4
print(14 % 3)  # remainder = 2

# Math Functions
print(round(3.1))  # rounding a number
print(abs(-20.1))  # absolute value (Modular function) = +20.1

# Binary number
print(bin(5))
print(int('0b101', 2))  # from a base 2

# Use multi line strings or paragraphs
long_string = '''
WOW
OO
---
'''

print(long_string)

# Tab, New line
weather = '\t \n New tab, new line'


name = 'Saugaat'
age = '12'

# Formatted String (or an f-string)
print(f'hi {name}. You are {age} years old')  # Python 3

print('hi {}. You are {} years old'.format(name, age))  # Python 2
print('hi {1}. You are {0} years old'.format(name, age))  # Python 2

a_string = '01234567'
print(a_string[0])
# [start:stop:stepover]
print(a_string[0:5])
print(a_string[0:5:2])  # prints 024
print(a_string[1:])  # prints 1234567
print(a_string[-2])  # starts from reverse; prints 6
print(a_string[::-1])  # Start from 0; end at 7; print in reverse; 76543210

print('*' * 10)  # Prints **********


li1 = ['orange', 'apple', 'grapes', 'banana']

print(li1)
li_new = li1  # This is still a reference

# To instead make a copy, use:
li_new = li1[:]

li_new[0] = 'wine'

print(li1)
print(li_new)


basket = ['a', 'b', 'c', 'd', 'e']
print('b' in basket)  # True

print(list(range(1, 100)))  # Prints an array from 1 to 100

# Join - A String method
# Use this to convert a list/array to a String
sentence = '_'.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(sentence)

# List unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = 1, other = [4,5,6,7,8], d = 9

# Dictionaries- Unordered key-value pair (Below is list of dict)
my_list = [{
    'a': [1, 2, 3],
    'b': "Hello"
},
    {
    'a': [4, 5, 6],
    'b': "There"
}]

print(my_list[1]['b'])

dictionary = {
    'an_array': [1, 2, 3],
    'a_string': "Hello"
}

# print(dictionary['age'])  # This will throw an error if key doesn't exist
print(dictionary.get('age'))  # This will return 'None'
print(dictionary.items())
print('an_array' in dictionary.keys())  # Prints True

# Tuple- Immutable lists
my_tuple = (1, 2, 3, 4, 5)
PI, CIRCLE = (3.14, 5)

# Sets - unordered collection of unique items
# Can also use sets like Venn Diagram Sets
my_set = {1, 2, 3, 3, 3, 3}  # Returns {1,2,3}
my_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
print(list(set(my_list)))  # In case want to remove duplicate usernames

# print(my_set | my_set2) # For Union
# print(my_set & my_set2) # For Intersection

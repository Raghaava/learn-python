# lists - Ordered collection

# hetrogenous
fhandle = open('input.txt')
list_example = [1, [0, 1], 2.0, 'Ragahva', fhandle]
for val in list_example:
    print(val)
# print all values
print(list_example)

# print size of list
print(len(list_example))

# lists are mutable
# [0, 1]
print(list_example[1])
list_example[1] = 'Hi'
# 'Hi'
print(list_example[1])

# Range function -> returns list.of numbers starting from 0 to one
# less than parameter value. we can use it in for loop.
# [0, 1, 2, 3]
print(range(4))

for i in range(len(list_example)):
    print(list_example[i])

# + operator can be used to join to lists.
print(list_example+list_example)

# slicing
print(list_example[1:3])

print(dir(list_example))

# create list from scratch
stuff = list()
stuff.append(1)
stuff.append('Raghava')
print(stuff)

# in operator
print('Raaghava' in stuff)

# sort list
stuff = ['Raghava', 'Gadde', 'Hari']
stuff.sort()
print(stuff)

# len, max, min, sum
# print(len(stuff), max(stuff), min(stuff), sum(stuff))

# Strings and lists
str = 'With three words'
words = str.split()
for word in words:
    print(word)
print(len(words))

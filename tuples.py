# tuples are more like lists
# but they are immutables for efficiency
# can be called read-only list

x = (1, 2, 'abc')
print(x[2])
for i in x:
    print(i)
# TypeError: 'tuple' object does not support item assignment
#   x[2] = 1
# not allowed sort, append, reverse

y = tuple()

print(dir(y))

# assignment
(x, y) = (1, 99)
print(x+y)
a = ('hi', 'bye')
print(a[0])

y = [(1, 3), (4, 5), (6, 7)]

for (k, v) in y:
    print(k, v)

# compare -> compare first element from both tuples and go on.
# it's short circuit.
print((0, 1, 2) < (0, 0, 5))

# sort tuples
# [('a', 10), ('c', 22), ('b', 1)]
print({'a': 10, 'c': 22, 'b': 1}.items())
# [('a', 10), ('b', 1), ('c', 22)]
print(sorted({'a': 10, 'c': 22, 'b': 1}.items()))

# bag of values, each with it's own label. unordered collection.

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 14
print(purse)
purse['candy'] = purse['candy']+2
print(purse)
purse[0] = 'Hi'
print(purse)

# Dictionary literals
map = {'chuck': 1, 'fred': 2, 'jan': 3}
print(map)

# counting
names = ['Raghava', 'Gadde', 'Raghava', 'Hari', "test"]

histogram = dict()
for name in names:
    if name not in histogram:
        histogram[name] = 1
    else:
        histogram[name] = histogram[name]+1
print(histogram)

# get -> get or give default values
print(histogram.get('hi', 'not found'))
histogram = dict()
for name in names:
    histogram[name] = histogram.get(name, 0)+1
print(histogram)

# count words in file
fhandle = open('input.txt')
map = dict()
for line in fhandle:
    words = line.strip().split()
    for word in words:
        map[word] = map.get(word, 0)+1
print(map)

# iterate through Dictionary
for key in map:
    print(key, map[key])

for value in map.values():
    print(value)

for key in map.keys():
    print(key)

for key, value in map.items():
    print(key+', ' + str(value))

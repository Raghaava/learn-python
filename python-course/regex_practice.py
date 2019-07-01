# ^ = begining
# $ = end
# . = match anything
# \s = any whitespace
# \S = non whitespace char
# * = Repeats a char 0 or more times.
# *? = non-greedy
# + = repeats char one more time.
# +? = non-greedy
# [aeiou] = matches a single character in the listed set.
# [^XYZ] = matches a signle character not lised in the set.
# [a-z0-9] = set of characters can include in the range.
# () = indicates where string extraction starts '(' and ends ')'

import re


fhandle = open('input.txt')

for line in fhandle:
    line = line.strip()
    # print only lines contains 're'
    # re.search gives true/false
    if re.search('re', line):
        print(line)

print('-----------')
fhandle = open('input.txt')

for line in fhandle:
    line = line.strip()
    # print only lines contains 're'
    if re.search('^th', line):
        print(line)

print('-----------')
x = 'My 2 favorite numbers are 19 and 42'
# findAll returns all matches
result1 = re.findall('[0-9].', x)
result2 = re.findall('[AEIOU]+', x)
# negate previous expression
result3 = re.findall('[^AEIOU]+', x)
print(result1)
print(result2)
print(result3)
print('-----------')
# greedy matching - > Always considers largest string after expanding
# both directions.
x = 'From: using the : character'
result = re.findall('^F.+:', x)
# ['From: using the :']
print(result)
# non-greedy - add ? (shortest string)
result = re.findall('^F.+?:', x)
# ['From:']
print(result)
print('-----------')

x = 'From raghav@gmail.com Sat Jan 5 09:16:17 2019'

result = re.findall('\S+@\S+', x)
print(result)
print('-----------')

# extracts from and till using ()

# 'From raghav@gmail.com'
result1 = re.findall('^From \S+@\S+', x)
# raghav@gmail.com'
result2 = re.findall('^From (\S+@\S+)', x)
print(result1)
print(result2)
print('-----------')
print(re.findall('@(\S+)', x))
print(re.findall('@([^ ]*)', x))
print(re.findall('^From .+@([^ ]*)', x))
print('-----------')
fhandle = open('input0.txt')
marks = list()
for line in fhandle:
    line = line.rstrip()
    mark = re.findall('marks:([0-9.]+)', line)
    if len(mark) == 0:
        continue
    marks.append(float(mark[0]))
print('avg '+str(sum(marks)/len(marks)))
print('-----------')

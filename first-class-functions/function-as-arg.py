# First class functions/objects typically can be assigned
# to a variable, passed as an argument and returned from function.


def square(num):
    return num*num


def cube(num):
    return num*num*num


# update function is taking another fun as an argument
def update(fun, arr):
    result = []
    for i in arr:
        result.append(fun(i))
    return result


# this fun is returnoing another function
def logger(msg):
    def log():
        print('log: ', msg)
    return log


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text


# assign fun to a variable
var1 = square
var2 = cube
print(var1(10))

print(update(var1, [1, 2, 3]))
print(update(var2, [1, 2, 3]))
var3 = logger("Hi")
print(var3())

var4 = html_tag('h1')
print(var4('Raghava'))

import logging
logging.basicConfig(filename='example.closure', level=logging.INFO)

# a closure is a record storing a function[a] together with an environment.
# The environment is a mapping associating each free variable of the function
# (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
# Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope


def closure_example(func):
    def execute(*args):
        logging.info('executing "{}" with args {}'.format(func.__name__, args))
        print(func(*args))
    return execute


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


addfun = closure_example(add)
addfun(1, 2)

subfun = closure_example(sub)
subfun(1, 2)

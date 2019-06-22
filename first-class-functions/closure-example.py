import logging
logging.basicConfig(filename='example.closure', level=logging.INFO)


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

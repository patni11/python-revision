'''
#Ternary Conditionals
x = 1 if True else 0
print(x)
'''

'''
# underscore Palceholder
num1 = 100_000_000_000
num2 = 1_000_000
total = num1 + num2
print(f'{total:_}')
'''

# context managers -> allows you to handle the opne and close fil situation or the thread situation or anything thaa treuqirest oepn and exit
# They can be used anywhere you have a situation where you need to go back to the previous state after finishing your task. It hndles resources automatically
"""
# understanding with the help of a class
class Open_file():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_file('array.py', 'r') as f:
    print(f.readlines())

print(f.closed)
"""

# Context Managers wiht function
'''
from contextlib import contextmanager
@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with open_file('array.py', 'r') as f:
    print(f.readlines())

print(f.closed)
'''

'''
# Ennumerate -  to print out position with the valuesn
names = ['thams', 'james', 'john', 'samantha']
for index, name in enumerate(names, start=1):
    print(index, name)

last_name = ['smit', 'john', 'carter', 'carol']
for name, last_name in zip(names, last_name):
    print(name, last_name)
'''

# Decorators -> Adds additional functionaluty to our original function without chanign our origitnal function

# Decorator Functions

# Practicla Example 1 - Logging -> To keep a track of what fucntion was run and how was it run
# Practise Example 2 - Timing Function




from functools import wraps
def logger(original_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        original_func.__name__), level=logging.INFO)

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        logging.info('The function [{}] ran with these args {} and kwargs {}'.format(
            original_func.__name__, args, kwargs))
        return original_func
    return wrapper


def function_timer(original_func):
    import time

    @wraps(original_func)
    def wrapper(*args, **kwargs):
        current_time = time.time()
        # running the original function to check its duration
        result = original_func(args, kwargs)
        time_taken = time.time() - current_time
        print("It took [{}] to run the [{}] function".format(
            time_taken, original_func.__name__))
        return result  # in this case we are returning the result so that when our original fucntion runs, with its tiken taken printed the result is also usable

    return wrapper

# WE CAN ALSO STACK DIFFERENT DECORATORS TOGETHER AND USE BOTH FUNCTIONAILTY. IF WE DO THAT IT WOULD LOOK SOMETHING LIKE THIS-
# @LOGGER
# @FUNCTION_TIMER
# DEF PRINT_NAME() .....
#
# THIS IS SAME AS SAYING
# PRINT_NAME = LOGGER(FUNCTION_TIMER(PRINT_NAME))
# SO WHENEVER WE RUN PRINT_NAME, THE ABOVE ACTIONS WILL TAKE PALCE AND THE OUTPUT OF TIMER_FUNCTION, WHICH IS A WRAPPER, WILL BE PASSED TO OUR LOGGER AND IT WILL CREATE A LOG FOR THAT FUCNTION
# TO FIX THAT WE CAN USE A WRAPPER DECORATOR FORM FUNCTOOLS LIBRARY. Now this will fix the issue and we will no see wrapper function returned from function time, but our print_name functoin


@logger
def fucn():
    print("THe Func Ran 100 Miles")


@function_timer
def print_name(name, last_name):
    print("My name is {} {}".format("Shubh", "Patni"))


# fucn()
#print_name("Shubh", "Patni")


# Decorator Class
'''

class decorator_class(object):

    def __init__(self, fucntion):
        self.fucniton = fucntion

    def __call__(self, *args, **kwargs):
        print("Class is running the decorator fucntion")
        return self.fucniton(*args, **kwargs)


@decorator_class
def fucn():
    print("THe Func Ran 100 Miles")


@decorator_class
def print_name(name, last_name):
    print("My name is {} {}".format("Shubh", "Patni"))


fucn()
print_name("Shubh", "Patni")
'''

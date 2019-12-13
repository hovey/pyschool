#!/usr/bin/env python
from functools import wraps

# def log_to_file  # to come

def log_to_screen(func):
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        print(f'\nLog: Function "{func.__name__}" was called with logging decorator.')
        return func(*args, **kwargs)
    return wrapped_func

@log_to_screen
def add_two(x, y):
    """An example dummy function."""
    return x + y

def add_three(x, y, z):
    """An example dummy function."""
    print(f'\nLog: Function "{add_three.__name__}" was called without the logging decorator.')
    return x + y + z

a, b, c = 1, 2, 3

result = add_two(a, b)
print(f'The add_two result is {result}.')

result = add_three(a, b, c)
print(f'The add_three result is {result}.')

print("\nLogging without decorators is W.E.T. (write everything twice).")
print("Every function call to be logged must implement logging.")

print("\nLogging with decorators is D.R.Y. (don't repeat yourself).")
print("Every function call to be logged implements nothing additional;")
print("it is simply decoratored with the logging decorator.")


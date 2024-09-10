# %%
from my_module.test import test


print(test())
# %%
def decorator1(func):
    def wrapper():
        print("Inside decorator1")
        # func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Inside decorator2")
        # func()
    return wrapper

@decorator1
# @decorator2
def my_function():
    print("Inside my_function")

my_function()
# %%
import random


def f(x=None):
    if x is None:
        x = random.random()
    return x


print(f(3.123))
print(f())

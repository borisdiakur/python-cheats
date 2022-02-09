def f(a, b, c=1, d=2):
    return a * b + c * d


print(f(1, 2))
print(f(b=2, a=1))
print(f(1, 2, d=4))

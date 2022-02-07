def f(x, l=[]):
    l += [x]
    return l


print(f(42))
print(f(3, [1, 2]))
print(f(43))

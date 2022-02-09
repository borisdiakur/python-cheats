a = list(range(10))

print(a)

print(list(filter(lambda x: x % 2 == 0, a)))
print(list(filter(lambda x: x >= 4, a)))
print(list(map(lambda x: x + 1, a)))

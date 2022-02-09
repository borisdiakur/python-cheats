def add_two(x):
    return x + 2


my_list = [add_two(a) for a in range(10)]
# my_list = [(lambda x: x + 2)(a) for a in range(10)]

print(my_list)

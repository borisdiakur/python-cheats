even_nums = [x for x in range(11) if x % 2 == 0]
print(even_nums)

odd_nums = list(filter(lambda x: x % 2 != 0, range(11)))
print(odd_nums)

all_smaller_10 = all(i < 10 for i in [1, 3, 5, 7])
print(all_smaller_10)

num_gen = (i for i in [1, 2, 3])
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))

two_dim_list = [[(x, y) for x in range(3)] for y in range(2)]
print(two_dim_list)

dct = {'a': 'A', 'b': 'B'}
keys = [*dct]
vals = [dct[key] for key in dct]
print(keys, vals)

dict_from_list = {i: x for i, x in enumerate(['a', 'b', 'c'])}
print(dict_from_list)

# sum_of_i_for_devidable_with_3 = sum(
#     [x for i, x in enumerate([-2, 8, 5, 9, 7, 7, 1]) if i % 3 == 0 and i > 0])
# print(sum_of_i_for_devidable_with_3)

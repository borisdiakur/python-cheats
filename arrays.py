# init
x = ['a', 3, 3j]
print(x)  # ['a', 3, 3j]

# length
print(len(['a', 'b']))
print(len(['a', 'b', ]))  # same

# append
x.append(None)
print(x)  # ['a', 3, 3j, None]

# prepend
x.insert(0, 4.4)  # or x = [4.4, *x]
print(x)  # [4.4, 'a', 3, 3j, None]

# slice
x = x[1:3]
print(x)  # ['a', 3]

# insert
x.insert(1, 'b')
print(x)  # ['a', 'b', 3]

# concatenate
x = x + [1, 7] + ['yolo']
print(x)  # ['a', 'b', 3, 1, 7, 'yolo']

# get at index
print(x[1])  # 'b'

# get at index from end (⚠️ starts with -1 ⚠️)
print(x[-1])  # 'yolo'

# print(x[10])  # out of range exception

# reverse
x.reverse()  # or x = reversed(x)
print(x)  # ['yolo', 7, 1, 3, 'b', 'a']

# entries at odd indices
print(x[1:len(x):2])  # [7, 3, 'a']

# entries at even indices
print(x[::2])  # ['yolo', 1, 'b']

# pop
x.pop()  # returns 'a'
print(x)  # ['yolo', 7, 1, 3, 'b']


# foreach with value and index
def foreach(function, iterable):
    for t in enumerate(iterable):
        function(t[1], t[0])


foreach(lambda val, i: print(val, i), ['a', 'b', 'c'])

# contains / has / exists
print('b' in ['a', 'b', 'c'])

# filter
print(list(filter(lambda val: len(val), ['a', 'b', '', 'c'])))

# map
print(list(map(lambda val: val.upper(), ['a', 'b', 'c'])))

# flatten
print([item for sublist in [[1, 2, 3], [4, 5]] for item in sublist])

# zip
print(list(zip([1, 2, 3], ['a', 'b'])))

for (num, char) in zip([1, 2, 3], ['a', 'b']):
    print(num, char)

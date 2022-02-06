# init
x = ['a', 3, 3j]
print(x)  # ['a', 3, 3j]

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

# length
print(len(x))

# get at index
print(x[1])  # 'b'

# get at index from end (⚠️ starts with -1 ⚠️)
print(x[-1])  # 'yolo'

# out of range
#  print(x[10])

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

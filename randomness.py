import random

# print random int between a and excluding b
print(random.randrange(3, 7))

# print random float between a and including b rounded to 1 decimal
print(round(random.uniform(1.8, 2), 3))
print(round(random.randrange(1800, 2000) * 0.001, 3))

# print random boolean
print(random.choice([True, False]))

# print random value from list
print(random.choice(['a', 'b', 'c']))

# print randomized list
lst = ['a', 'b', 'c', 'e', 'f', 'g']
random.shuffle(lst)
print(lst)

# print random sample from a list
lst = ['a', 'b', 'c', 'e', 'f', 'g']
print(random.sample(lst, 3))

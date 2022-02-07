s1 = {'Mochi', 'Kimchi', 'Kimchi'}

print(s1)  # {'Mochi', 'Kimchi'}

s2 = {'Mochi', 'Chichi', 'Naonao'}

print(s1 | s2)  # {'Kimchi', 'Chichi', 'Mochi', 'Naonao'}
print(s1 & s2)  # {'Mochi'}
print(s1 - s2)  # {'Kimchi'}
print(s1 ^ s2)  # {'Kimchi', 'Naonao', 'Chichi'}

dynamic_key = 'yolo'
cat = {'name': 'Mochi', 'legs': 4, dynamic_key: 'CHACKA!'}

print(cat[dynamic_key])

for key in cat:
    print(key, cat[key])

print(*cat)  # name legs yolo

print(cat.get('does_not_exist'))  # -> None

dynamic_key = 'yolo'
cat = {'name': 'Mochi', 'legs': 4, dynamic_key: 'CHACKA!'}

print(cat.get(dynamic_key))
print(cat.get('name'))
print(cat.get('yolo'))

keys = [*cat]
vals = [cat[key] for key in cat]
print(keys, vals)

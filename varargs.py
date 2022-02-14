def yolo(name, *args, **darks):
    print(name)
    for a in args:
        print(a)

    if 'bla' in darks:
        print(darks['bla'])


yolo('Mochi', 'Kimchi', 'Naonao', bla='Chichi')

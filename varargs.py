def yolo(name, *args, **darks):
    print(name)
    for a in args:
        print(a)

    for key in darks:
        print(darks[key])


yolo('Mochi', 'Kimchi', 'Naonao', bla='Chichi')

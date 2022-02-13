class A(Exception):
    pass


class B(A):
    pass


for cls in [A, B, Exception('yolo')]:
    try:
        raise cls()
    except B:
        print("B")
    except A:
        print("A")
    except (Exception,):
        print("uups")

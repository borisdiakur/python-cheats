# Python has function scope

def yolo():
    global x
    x = 3


x = 2
yolo()
print(x)

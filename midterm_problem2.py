from math import cos, radians, sin

def partC():
    l1 = 60
    l2 = 40
    d = -14

    x = l1 * cos(radians(30)) + l2 * cos(radians(30+45))
    y = l1 * sin(radians(30)) + l2 * sin(radians(30+45))
    
    print("x =", x, "y =", y, "z =", d)


partC()
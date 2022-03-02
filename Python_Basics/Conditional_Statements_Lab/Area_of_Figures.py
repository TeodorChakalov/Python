from math import pi
import math

figure = input()

if figure == "square":
    a = float(input())
    area = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    # print('{0:.3f}'.format(a * b))
    # print(round(area, 3))
elif figure == "circle":
    r = float(input())
    area = pi * r * r
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
print(f"{area:.3f}")
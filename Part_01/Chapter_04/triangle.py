# cchapter 4 Programming Puzzel

# A triangle

import turtle
import math

t = turtle.Pen()

t.forward(100)

t.left(120)

t.forward(100)

t.left(120)

t.forward(100)

t.left(120)

A = 100
B = 100
C = 50

a_in_radian = math.acos((math.pow(A,2)+ math.pow(C,2)- math.pow(B,2))/(2*A*C))

print(a)

a_in_degree = math.degrees(a)

print(a)

t.forward(C)

t.left(180-a_in_degree)

t.forward(A)

t.left(2*a_in_degree)

t.forward(B)



import turtle
from turtle import *
t = Turtle()
t.speed(1000)

for i in range(100):
    def square(x):
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
    square(200)
    t.left(5)

turtle.done()


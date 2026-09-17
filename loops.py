import turtle
from turtle import *
t = Turtle()
t.speed(1000)
   
""" def square(x,y):
    t.forward(x)
    t.left(y)
    t.forward(x)
    t.left(y)
    t.forward(x)
    t.left(y)
    t.forward(x)
    t.left(y)
for i in range(100):
    square(200,90)   
    t.left(5)

turtle.done() 

 """


def doubleSquares(iRange):
    length = 5
    for i in range (iRange):
    square(length, 90)
    length = length * 1.15
    t.right(5)
doubleSquares(60)
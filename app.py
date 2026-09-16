import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
 
""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
square(200) """

""" def equal(x):
    t.forward(x)
    t.left (120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) """

def right():
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(135)
    t.forward(285)
right()
turtle.done() 
 

""" def add(x,y):
    #variables here only accessible in the function, SCOPE
    return x + y
    #call to function
 z= add(5,15) """
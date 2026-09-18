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

""" sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90)

def doubleSquares(iRange):
    length = 15
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(100)
  """

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(7,90)

def doubleSquares(iRange):
    length = 5
    for i in range (iRange):
        square(length, 90)
        length = length * 1.07
        t.right(5)
doubleSquares(60)
turtle.done() """

def triangle(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
triangle(5,144)

def doubleTriangles(iRange):
    length = 8
    for i in range(iRange):
        triangle(length, 144)
        length = length * 1.07
        t.right(5)
doubleTriangles(60)
turtle.done()




""" #data types, 1. Strings name = "text" (strings are for characters.)
#input asks theuser a question and records the answer.
# what we write in input arguement is what user sees.
#input always outputs a string
name = "kevin"
print(name.lower().capitalize())
bill = int(input("How much was the bill"))
print("bill")

if bill ==10:
    print("match")
else:
    print("not a match.")
#integer for whole number
amt = 100
#Float uses decimal
amt_two = 99.99

#Boolean 
x = True
y = False """

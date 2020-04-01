# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 07:49:14 2020

@author: George
"""

"""
# Challenge 5 - turtles

Each of these challenges requires you to use the skills you have so far learnt, as well as a couple of new things. They give you the chance to practice core concepts and improve your skills reading/researching code.

This is the fifth Python challenge.

### Prerequisites

Before completing this challenge, you should be familiar with the following Python topics:

1. importing
2. writing functions

### New learning

In order to complete this challenge, you will need to research the Python turtle module.

### Challenge requirements

1. In no more than 3 lines of code, write instructions for a turtle to draw a triangle
2. Use a turtle to draw a square inside a triangle inside a circle. No shape should touch any other
3. Write a function that tells a turtle to draw a square of a user-inputted size
4. Write a function that tells a turtle to draw a shape with a given number of sides

### Guidance

If you are programming in either Jupyter notebooks or Trinket, you will not be able to easily run the turtle module in your normal development environment. Instead, you should use the [Turtle Trinket](https://trinket.io/turtle).

If you get stuck on this challenge, the best option is to look online for help and examples of similar problems. There is also a [walkthrough](../walkthroughs/5.md) you can refer to when nothing else helps.
"""



# create a turtle
from turtle import Turtle

belinda = Turtle()

# set the speed to the highest setting
belinda.speed(100)

# draw a square
for i in range(4):
  belinda.forward(50)
  belinda.right(90)

# move the turtle
belinda.penup()

belinda.back(50)
belinda.right(90)
belinda.forward(55)
belinda.left(90)

belinda.pendown()

# draw a triangle
for i in range(3):
  belinda.forward(150)
  belinda.left(120)

# move the turtle
belinda.penup()

belinda.back(40)
belinda.right(90)
belinda.back(50)

belinda.pendown()

# draw a circle
for i in range(360):
  belinda.forward(2)
  belinda.left(1)

# square function

def draw_square(turtle, length):
  for i in range(4):
    turtle.forward(length)
    turtle.right(90)

# shape function
def draw_shape(turtle, sides, length):
  for i in range(sides):
    turtle.forward(length)
    turtle.right(360/sides)
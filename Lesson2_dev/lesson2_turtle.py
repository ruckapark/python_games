# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:11:15 2020

@author: George
"""

#%%
import turtle

george = turtle.Turtle()

# set the speed to the highest setting
george.speed(1)

# draw a square
for i in range(4):
  george.forward(50)
  george.right(90)

# move the turtle
george.penup()

george.back(50)
george.right(90)
george.forward(55)
george.left(90)

george.pendown()

# draw a triangle
for i in range(3):
  george.forward(150)
  george.left(120)

# move the turtle
george.penup()

george.back(40)
george.right(90)
george.back(50)

george.pendown()

# draw a circle
for i in range(360):
  george.forward(2)
  george.left(1)
  
import random
turtle.clearscreen()
def circle(turtle_):
    
    colors = 'red blue green yellow black'.split()
    
    x = random.randint(-150,150)
    y = random.randint(-150,150)
    radius = random.randint(10,70)
    color_line = colors[random.randint(0,4)]
    color_fill = colors[random.randint(0,4)]
    thickness = random.randint(0,radius//2)
        
    
    turtle_.penup()
    turtle_.goto(x,y)
    turtle_.pendown()
    turtle_.pensize = thickness
    turtle_.color(color_line,color_fill)
    turtle_.begin_fill()
    turtle_.circle(radius)
    turtle_.end_fill()
        

for i in range(10):
    circle(george)

turtle.Screen().exitonclick()    
turtle.done()
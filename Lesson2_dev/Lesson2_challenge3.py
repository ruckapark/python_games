# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 10:49:25 2020

@author: George
"""
import turtle
import random

colors = ['red','blue','green','black','orange','purple','yellow','white']
num_colors = len(colors)
#screen width and height
width,height = 300,200

def rand_col():
    return colors[random.randint(0,num_colors-1)]

def circle(turtle_):
    
    x = random.randint(-width,width)
    y = random.randint(-height,height)
    
    #generate random radius for the circles
    radius = random.randint(10,70)
    color_line = rand_col()
    color_fill = rand_col()
    thickness = random.randint(0,radius//10)
        
    #don't want to draw the process of moving to the coordinates
    turtle_.penup()
    turtle_.goto(x,y)
    turtle_.pendown()
    turtle_.pensize(thickness)
    turtle_.color(color_line,color_fill)
    #as with in the lesson (function is the same)
    turtle_.begin_fill()
    turtle_.circle(radius)
    turtle_.end_fill()

george = turtle.Turtle()    
screen = turtle.Screen()
screen.clearscreen()
screen.bgcolor("green")
for i in range(50):
        circle(george)

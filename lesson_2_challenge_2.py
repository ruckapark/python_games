# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 07:49:14 2020

@author: George
"""

"""
# Challenge - turtles

### Guidance

MAKE SURE YOU READ THE DESCRIPTION IN THE CHALLENGES2 NOTEBOOK FILE!
"""



# create a turtle
from PIL import ImageGrab,Image
import turtle
import os
import random

"""
Taking inspiration from one of the backgrounds we made for flappy bird, make one more background of the same size, using turtle

Here is a code for one that I made that you can use as inspiration!

It shows how I saved it as a picture.
"""

#screen dims
height = 500
width = 1920//2
IMG_FILENAME = 'bg_turtle.jpg'

def hex_col(r_limit = False,g_limit = False,b_limit = False):
    if r_limit:
        r = str(hex(random.randint(0,125))).upper()[2:]
    else:
        r = str(hex(random.randint(0,255))).upper()[2:]
    if len(r) == 1:
        r = r + '0'
        
    if g_limit:
        g = str(hex(random.randint(0,125))).upper()[2:]
    else:
        g = str(hex(random.randint(0,255))).upper()[2:]
    if len(g) == 1:
        g = g + '0'
    
    if b_limit:
        b = str(hex(random.randint(0,125))).upper()[2:]
    else:
        b = str(hex(random.randint(0,255))).upper()[2:]
    if len(b) == 1:
        b = b + '0'
    
    return '#{}{}{}'.format(r,g,b)

def circle(turtle_):
    
    x = random.randint(-width//2 + 70,width//2 - 70)
    y = random.randint(-50,200)
    radius = random.randint(10,70)
    color_line = hex_col(b_limit = True) #dont want sky color outline
    color_fill = hex_col(g_limit = True,b_limit = True)
    color_fill = '#FF' + color_fill[3:]
    thickness = random.randint(0,radius//10)
        
    
    turtle_.penup()
    turtle_.goto(x,y)
    turtle_.pendown()
    turtle_.pensize(thickness)
    turtle_.color(color_line,color_fill)
    turtle_.begin_fill()
    turtle_.circle(radius)
    turtle_.end_fill()
    
def hill(turtle_):
    hill_max = 100 #max radius of hill
    x = random.randint(-width//2 + hill_max,width//2-hill_max)
    y = -350
    
    radius = random.randint(70,hill_max)
    color_line = 'purple'
    color_fill = 'green'
    thickness = 8
        
    
    turtle_.penup()
    turtle_.goto(x,y)
    turtle_.pendown()
    turtle_.pensize(thickness)
    turtle_.color(color_line,color_fill)
    turtle_.begin_fill()
    turtle_.circle(radius)
    turtle_.end_fill()

def quarter_image(show = False):
    
    screen = turtle.Screen()
    screen.setup(width+50, height+50, startx = 50, starty = 50)
    screen.clearscreen()
    
    #make sure screen appears on top!
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    
    george = turtle.Turtle()
    george.speed(0)
    george.ht()
    
    #hexidecimal input! - can you work that one out?
    screen.bgcolor("#00B0F9")
      
    george.penup()
    george.pendown()
    for i in range(5):
        hill(george)
        
    for i in range(50):
        circle(george)

    im = ImageGrab.grab((75,100,width+75,height+100))
    if show: im.show()
    return im

#make a blank PIL image of width 1920 and height 500
    
bg_turtle = Image.new('RGB',(1920,500))
for i in range(4):
    im = quarter_image()
    bg_turtle.paste(im,(i*width,0))
bg_turtle.show()
bg_turtle.save('bg_turtle.jpg')
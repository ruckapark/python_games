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
    """
    Returns an r,g,b colour in the form of hex code. Look up hexidecimal if unsure (like binary but with 16 not 2!).
    If any parameter is input with a limit (i.e. g_limit = True) then it will only between 0-125 dimming that colours presence.
    For mainly red shades - limit green and blue...
    
    0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F
    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
    255 -> FF = (16^1)*15 + (16^0)*15 = 255
    11 -> B = (16^0)*11 = 11
    124 -> 7C = (16^1)*7 + (16^0)*12 = 124
    """
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
    """
    input the turtle to draw a random size and colour circle at the point x,y on you screen
    
    color_line = border colour
    color_fill = fill colour
    I want mainly red shade for the circles (weird clouds), and less blue for the borders (matches background)
    """
    
    x = random.randint(-width//2 + 70,width//2 - 70)
    y = random.randint(-50,200)
    #generate random radius for the circles
    radius = random.randint(10,70)
    color_line = hex_col(b_limit = True) #dont want sky color outline
    color_fill = hex_col(g_limit = True,b_limit = True)
    color_fill = '#FF' + color_fill[3:]
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
    
def hill(turtle_):
    """
    If I would like to make a green hill at the bottom of the screen, I can
    place the centre of a green circle just below the bottom of the screen so that we only see some of the top half.
    """
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
    """
    I want my background to be 1920 pixels wide.
    An easy portion to draw once is 1920/4 pixels wide (remember to int divide)
    then it will fit on my computer screen and I can just PIL screengrab function to save it as an image.
    """
    
    #make the screen a turtle object
    screen = turtle.Screen()
    #give extra height and width than necessary to ensure screengrab is within the borders!
    screen.setup(width+50, height+50, startx = 50, starty = 50)
    #for each repeat clear screen
    screen.clearscreen()
    
    #make sure screen appears on top of the windows (may happen automatically)
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    
    #assign my turtle object
    george = turtle.Turtle()
    george.speed(0)
    #make turtle invisible even with pendown()
    george.ht()
    
    #hexidecimal input! - can you work that one out? - I wanted a light blue background
    screen.bgcolor("#00B0F9")
    
    #draw five hills and 50 clouds at random places within the bounds
    george.penup()
    george.pendown()
    for i in range(5):
        hill(george)
        
    for i in range(50):
        circle(george)

    im = ImageGrab.grab((75,100,width+75,height+100))
    #if you want to double check it worked input show = True in the main function!
    if show: im.show()
    return im

#make a blank PIL image of width 1920 and height 500 to paste each screen grab into    
bg_turtle = Image.new('RGB',(1920,500))
for i in range(4):
    im = quarter_image()
    bg_turtle.paste(im,(i*width,0))
bg_turtle.show()
os.chdir('Flappy_bird_backgrounds')
bg_turtle.save('bg_turtle.jpg')
os.chdir('..')

#make a new code of your own copying the syntax (maybe add a house somewhere? Some squares (multicolours background? etc.))
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:15:23 2020

pygame setup

pygame is a wrapper between python and SDL library on our computer
SDL - Simple DirectMedia Layer gives cross-platform access to multimedia (sound, video, mouse, keyboard etc.)

@author: George
"""

# Simple pygame program

#%% 1. Import and initialize the pygame library
"""
go to the cmd and pip install pygame (hopefully this will work)
"""
import pygame

#%% 2. remember the init() command - otherwise the machine won't initialise the 
pygame.init()

# Set up the drawing window as a square of 500 by 500 pixels - i prefer a tuple as the screen size does not change
screen = pygame.display.set_mode((500, 500))

#%% 3. Setup a dictionary with some colours in it

colours = 'red green blue darkBlue white black pink'.split()
rgb_values = [(255,0,0),(0,255,0),(0,0,255),(0,0,128),(255,255,255),(0,0,0),(255,200,200)]
colour_dict = dict(zip(colours, rgb_values))

#%% 4. A quick game loop with no game
"""
1.  Fill the screen with a colour - remember from before how the colour system works
    As we have already setup the screen as a pygame display object we can use the fill() command followed by any r,g,b value
2.  Use the draw module in pygame to put some shapes on the screen
    Parameters for lines: (screen, color, closed, pointlist)
    Parameters for circle: (screen, color, (x,y), radius)
    Parameters for rect: (screen, color, (x,y,width,height))
3.  Remember at the end of each iteration to update the display or we won't see anything that has been drawn
4.  Events are when the keyboard signals that something been pressed.
    If we call pygame.event.get() it returns a list of all the events since the last iteration
    One for example is QUIT which is when we click on the exit icon at the top right
    We can iterate through our events to tell the computer if we have exited or alternatively if we have move left or right
    Let's try to print something whenever we press anything and the exit the screen if we press exit
"""
# Run until the user asks to quit
running = True
while running:

    # Fill the background with black
    screen.fill(colour_dict['black'])

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, colour_dict['pink'], (250, 250), 75)
    pygame.draw.lines(screen, colour_dict['white'], False, [(0,175),(500,175)])
    pygame.draw.lines(screen, colour_dict['white'], False, [(0,225),(500,225)])
    pygame.draw.rect(screen, colour_dict['black'],(250,250,30,20))
    
    #5. Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print('Something is pressed')
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    
#6. Done! Time to quit. If we break out of the loop remember to shut the window down.
pygame.quit()
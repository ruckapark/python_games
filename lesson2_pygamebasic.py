# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:43:16 2020

@author: George
"""

import pygame

pygame.init()
width, height = 800,600
backgroundColor = (255,0,0) #red
rectColor = (0,0,255) #blue
rect_x,rect_y = 0,0
rect_w,rect_h = 50,50

#this is the game screen - when we draw something we have to tell it to draw on the screen
screen = pygame.display.set_mode((width, height))

running = True
while running:
    screen.fill(backgroundColor)
    pygame.draw.rect(screen,rectColor,(rect_x,rect_y,rect_w,rect_h))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
                rect_x = rect_x - 10
            elif event.key == pygame.K_RIGHT:
                print('right')
                rect_x = rect_x + 10
    
    pygame.display.update()
pygame.quit()
"""
Exercises:
    1. play around with the colors (rectColor and backgroundColor) by changing the numbers
       Try to make the background green. Try to make the square yellow or purple (you can google RGB colours)
       
    2. Add two more elif event.key statements with K_UP and K_DOWN and see if you can make the rect
       Go up and down (you will have to change rect_y instead of rect_x this time!)
"""
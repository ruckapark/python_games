# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:34:05 2020

pygame space invaders main

@author: George
"""

import pygame

#pygame initialisation
pygame.init()

#create the screen that we want to play on
#notice that after inserting this line we might only see the window briefly
#nothing is telling the programme to keep running!
screen = pygame.display.set_mode((800,600))

#1 Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("CVphoto.jpg") #use python emblem
pygame.display.set_icon(icon)

#unless we create a quit functionality we can't shut the window
running = True
#make sure the screen stays up
while running:
    #the game keeps running, we press buttons that get stored in event!
    for event in pygame.event.get(): #keep looping through the lise of events
        if event.type == pygame.QUIT:#stop running the while loop if we close it
            running = False
    
    #lets modify what this background looks like
    #try color to rgb!        
    screen.fill((0,200,0)) #rgb like we did before!
    pygame.display.update() #otherwise the pygame screeen will stay black
    
    
    
    
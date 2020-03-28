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
screen = pygame.display.set_mode((800,600))

#1 Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("CVphoto.jpg")
pygame.display.set_icon(icon)

#unless we create a quit functionality we can't shut the window
running = True
#make sure the screen stays up
while running:
    #turn false with the close event
    for event in pygame.event.get(): #keep looping through the lise of events
        if event.type == pygame.QUIT:
            running = False
            
    
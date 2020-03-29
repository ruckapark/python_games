# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 13:58:53 2020

@author: George
"""

import pygame
import os
pygame.init()

#%% 1. instead of having to type pygame.SPACE everytime we can just import them as local variables and type SPACE instead. This will save time later

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    KEYUP,
    QUIT,
)

colours = 'red green blue darkBlue white black pink'.split()
rgb_values = [(255,0,0),(0,255,0),(0,0,255),(0,0,128),(255,255,255),(0,0,0),(255,200,200)]
colour_dict = dict(zip(colours, rgb_values))

#%% 2. make the code more readable than the previous version and add a different title and icon

screen_w,screen_h = 500,500                             #screen size
screen = pygame.display.set_mode((screen_w, screen_h))  #display screen

pygame.display.set_caption("Space Invaders")

os.chdir('SI_pictures')
icon = pygame.image.load("SI_icon.jpg")
pygame.display.set_icon(icon)

#%% 3. Load in the image for the background, player icon, enemy and bullet - hopefully after lesson2 all these should be appropriate sizes
"""
When we make the second game we will introduce classes
"""

background = pygame.image.load('background.jpg') #moving background? - challenge
player = pygame.image.load('player_icon.PNG')
enemy = pygame.image.load('space_invader.PNG')
bullet = pygame.image.load('bullet.PNG')
os.chdir('..')

#assume all character square
player_size = 64
enemy_size = 32
bullet_size = 32

#%% 4. blit the images in to their desired locations - think about this relative to their size and screen size

running = True
while running:
    
    #in reality we reprint the images repeatedly! - so if we want them to move we will just have to update the values in the blit.
    screen.fill(colour_dict['black'])
    screen.blit(background,(0,0))
    screen.blit(player,((screen_w - player_size)/2,screen_h - 2*player_size))
    screen.blit(bullet,((screen_w - bullet_size)/2,screen_h/2))
    screen.blit(enemy,((screen_w - enemy_size)/2,2*enemy_size))
    
    #not how we now just type the command directly
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print('Something was pressed')
        if event.type == QUIT:
            running = False
    
    pygame.display.update()
    
pygame.quit()
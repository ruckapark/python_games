# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:07:57 2020

@author: George
"""

import pygame
import os
import random
pygame.init()

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

base_dir = os.getcwd() #store original directory

colours = 'red green blue darkBlue white black pink'.split()
rgb_values = [(255,0,0),(0,255,0),(0,0,255),(0,0,128),(255,255,255),(0,0,0),(255,200,200)]
colour_dict = dict(zip(colours, rgb_values))

screen_w,screen_h = 500,500                             #screen size
screen = pygame.display.set_mode((screen_w, screen_h))  #display screen

pygame.display.set_caption("Space Invaders")

os.chdir('SI_pictures')
icon = pygame.image.load("SI_icon.jpg")
pygame.display.set_icon(icon)

background = pygame.image.load('background.jpg') #moving background? - challenge


#%% 1. Let's split up the variables for player, bullet and enemy.

player = pygame.image.load('player_icon.PNG')
player_size = 64
playerX = (screen_w - player_size)/2    #will change - just starting value
playerY = screen_h - 2*player_size      #never changes


bullet = pygame.image.load('bullet.PNG')
bullet_size = 32
bulletX = playerX                       #initial trajectory
bulletY = playerY + bullet_size/2       #will change - negative direction

#%% 2. We are going to introduce multiple enemies which we will store in a list
enemy = []
enemy_size = 32
enemyX = []
enemyY = []
difficulty = int(input('How many enemies do you want to fight?'))
for i in range(difficulty):
    enemy.append(pygame.image.load('space_invader.PNG'))
    enemyX.append(random.randint(5,screen_w - enemy_size - 5))
    enemyY.append(2*enemy_size)

#%% 3. Account for the multiple enemies and add the event key for shooting and moving
running = True
while running:
    
    #in reality we reprint the images repeatedly! - so if we want them to move we will just have to update the values in the blit.
    screen.fill(colour_dict['black'])
    screen.blit(background,(0,0))
    screen.blit(player,(playerX,playerY))
    for i in range(difficulty):
        screen.blit(enemy[i],(enemyX[i],enemyY[i]))
    
    screen.blit(bullet,(bulletX,bulletY))
    #not how we now just type the command directly
    for event in pygame.event.get():
        
        #print in command if anything gets pressed, and if it is a left or a right
        if event.type == KEYDOWN:
            print('Something was pressed')
            if event.key == K_LEFT:
                print('Move Left')
            elif event.key == K_RIGHT:
                print('Move Right')
            
            if event.key == K_SPACE:
                print('SHOOT')
                
        #we want the release of the key to stop the movement
        if event.type == KEYUP:
            if event.key == K_LEFT:
                print('Stop Moving Left')
            elif event.key == K_RIGHT:
                print('Stop Moving Right')
        if event.type == QUIT:
            running = False
    
    pygame.display.update()
    
os.chdir(base_dir)
pygame.quit()
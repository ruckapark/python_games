# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:32:54 2020

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

#%% 1. account for bullet being on (1) and off (0), as well as the movement of the enemies and the player icon 

player = pygame.image.load('player_icon.PNG')
player_size = 64
playerX = (screen_w - player_size)/2    #will change - just starting value
playerY = screen_h - 2*player_size      #never changes
player_direc = 0 #not moving to start with (1 = right, -1 = left)
player_speed = speed = 5


bullet = pygame.image.load('bullet.PNG')
bullet_size = 32
bulletX = playerX                       #initial trajectory
bulletY = playerY + bullet_size         #will change - negative direction
bullet_speed = 8
bullet_on = 0

enemy = []
enemy_size = 32
enemyX = []
enemyY = []
enemy_direc = []
enemy_speed = 3
difficulty = int(input('How many enemies do you want to fight?'))
for i in range(difficulty):
    enemy.append(pygame.image.load('space_invader.PNG'))
    enemyX.append(random.randint(5,screen_w - enemy_size - 5))
    enemyY.append(2*enemy_size)
    enemy_direc.append(random.randint(0,1))
    if not enemy_direc[i]: enemy_direc[i] = -1
    
#%% 2. Add object functions to blit them to the screen

def player_(x,y):
    screen.blit(player,(x,y))
def enemy_(x,y,i):
    screen.blit(enemy[i],(x,y))

def fire_(x,y):
    screen.blit(bullet,(x,y))

running = True
while running:
    
    #in reality we reprint the images repeatedly! - so if we want them to move we will just have to update the values in the blit.
    screen.fill(colour_dict['black'])
    screen.blit(background,(0,0))
    
    #show player and enemies
    player_(playerX,playerY)
    for i in range(difficulty):
        enemy_(enemyX[i],enemyY[i],i)
    if bullet_on:
        fire_(bulletX,bulletY)
    
    #not how we now just type the command directly
    for event in pygame.event.get():
        
        #print in command if anything gets pressed, and if it is a left or a right
        if event.type == KEYDOWN:
            print('Something was pressed')
            if event.key == K_LEFT:
                player_direc = -1
            elif event.key == K_RIGHT:
                player_direc = 1
            
            if event.key == K_SPACE:
                bullet_on = 1
                bulletX = playerX
                fire_(bulletX,bulletY)
                
        #we want the release of the key to stop the movement
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player_direc = 0
                
        if event.type == QUIT:
            running = False
    
    #update the loaction of the player
    playerX += player_direc * player_speed
    #check it hasn't exceeded its bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= (screen_w - player_size):
        playerX = screen_w - player_size
    
    #update the location of the enemies
    for i in range(difficulty):
        enemyX[i] += enemy_direc[i] * enemy_speed
        #change direction and descend if it reaches the edge
        if enemyX[i] <= 0 or enemyX[i] >= screen_w - enemy_size:
            enemy_direc[i] = enemy_direc[i] * -1
            enemyY[i] += enemy_size
        
    #add bullets and see if they have left the screen
    if bullet_on:
        bulletY -= bullet_speed
        if bulletY <= 0:
            bulletY = playerY + bullet_size
            bullet_on = 0
    
    #update display at each iteration
    pygame.display.update()
    
os.chdir(base_dir)
pygame.quit()
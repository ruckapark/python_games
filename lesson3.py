# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:34:05 2020

pygame space invaders main

@author: George
"""

#%%

import pygame
import os
import random

#pygame initialisation
pygame.init()

#create the screen that we want to play on
#notice that after inserting this line we might only see the window briefly
#nothing is telling the programme to keep running!
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)

#1 Title and Icon
pygame.display.set_caption("Space Invaders")
os.chdir('Game_pictures')
icon = pygame.image.load("CVphoto.jpg") #use python emblem
pygame.display.set_icon(icon)

#%% Add player to a certain location

playerImg = pygame.image.load('player_icon.PNG')
space_invador = pygame.image.load('space_invador.PNG')
os.chdir('..')
#the player image is pixeled in the same way so we have to take size in to get the middle
player_size = (64,64)
enemy_size = (16,16) #make this automatic?
#try playing around with these values - what happens?
playerX_zero = (screen_size[0] - player_size[0])//2
playerY_zero = (screen_size[1] - player_size[1]) - 100
playerX,playerY = playerX_zero,playerY_zero
enemyX, enemyY = random.randint(0,screen_size[0]-enemy_size[0]),50 #make it a random location

direc = 0
enemy_direc = enemyX%2
if not enemy_direc: enemy_direc -= 1

#add boundaries so our player can't leave the board
Xmin,Xmax_player,Xmax_enemy = 0,screen_size[0]-player_size[0],screen_size[0]-enemy_size[0] #could index 1 and see if they can debug

#ask user how fast they want to go
speed = float(input('From 0.1 - 1, how fast do you want to move?'))
enemy_speed = float(input('From 0.1 - 1, how fast do you want enemies to move?'))

def player(x,y):
    """
    blit is like drawing on a game screen. Each frame we want out program to blit the player character on the game screen
    """
    screen.blit(playerImg, (x,y))
    
def enemy(x,y):
    screen.blit(space_invador, (x,y))

#%%

#unless we create a quit functionality we can't shut the window
running = True
#make sure the screen stays up
while running:
    
    #lets modify what this background looks like
    #try color to rgb!        
    screen.fill((0,200,0)) #rgb like we did before!
    
    #player must be after the screen fill!
    player(playerX,playerY)
    enemy(enemyX,enemyY)    #as soon as we put this in check its there
    pygame.display.update() #otherwise the pygame screeen will stay black
    
    # playerX += 0.1 # to move right slowly
    
    #the game keeps running, we press buttons that get stored in event!
    for event in pygame.event.get(): #keep looping through the lise of events
        if event.type == pygame.QUIT:#stop running the while loop if we close it
            pygame.quit()    #shut game window
            running = False  #stop python program
            
        # check for a keystroke event (left or right)
        if event.type == pygame.KEYDOWN:
            print('Something is pressed')
            if event.key == pygame.K_LEFT:
                direc = -1
                print('moving {}'.format(direc))
            elif event.key == pygame.K_RIGHT:
                direc = 1
                print('moving {}'.format(direc))
                
        #have to stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('direction released')
                direc = 0
           
    playerX += direc*speed
    enemyX += enemy_direc * enemy_speed
    
    if playerX <= Xmin:
        playerX = Xmin
    elif playerX >= Xmax_player:
        playerX = Xmax_player
        
    if enemyX <= Xmin or enemyX >= Xmax_enemy:
        enemy_direc = -enemy_direc
        enemyY += 25
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:34:05 2020

pygame space invaders main

@author: George
"""

#%%

import pygame
import os

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
os.chdir('..')
#the player image is pixeled in the same way so we have to take size in to get the middle
player_size = (64,64)
#try playing around with these values - what happens?
playerX = screen_size[0]/2 - player_size[0]/2
playerY = (screen_size[1] - player_size[1]) - 100

def player():
    """
    blit is like drawing on a game screen. Each frame we want out program to blit the player character on the game screen
    """
    screen.blit(playerImg, (playerX,playerY))

#%%

#unless we create a quit functionality we can't shut the window
running = True
#make sure the screen stays up
while running:
    
    #lets modify what this background looks like
    #try color to rgb!        
    screen.fill((0,200,0)) #rgb like we did before!
    
    #the game keeps running, we press buttons that get stored in event!
    for event in pygame.event.get(): #keep looping through the lise of events
        if event.type == pygame.QUIT:#stop running the while loop if we close it
            pygame.quit()    #shut game window
            running = False  #stop python program
    
    #player must be after the screen fill!
    player()
    pygame.display.update() #otherwise the pygame screeen will stay black
    
    
    
    
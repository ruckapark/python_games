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

#this can be a challenge addition - no need for the background in the working game
background = pygame.image.load('background.jpg') #moving background? - challenge

difficulty = int(input('How many enemies do you want?'))

playerImg = pygame.image.load('player_icon.PNG')
space_invador = [pygame.image.load('space_invador.PNG') for i in range(difficulty)]
bullet = pygame.image.load('bullet.PNG')
os.chdir('..')

#%%
#the player image is pixeled in the same way so we have to take size in to get the middle
player_size = (64,64)
enemy_size = (32,32) #make this automatic?
bullet_size = enemy_size #assume same sizes
#try playing around with these values - what happens?
playerX_zero = (screen_size[0] - player_size[0])//2
playerY_zero = (screen_size[1] - player_size[1]) - 100
playerX,playerY = playerX_zero,playerY_zero

bulletX, bulletY = 0,playerY
bullet_speed = 10 #moving back up y axis
bullet_state = 0 #unfired
bullet_distance = 100

enemyX,enemyY,enemy_direc = [],[],[]
for i in range(difficulty):
    enemyX.append(random.randint(0,screen_size[0]-enemy_size[0]))
    enemyY.append(50)
    enemy_direc.append(enemyX[i]%2)
    if not enemy_direc[i]: enemy_direc[i] = -1

score = 0
direc = 0

#add boundaries so our player can't leave the board
Xmin,Xmax_player,Xmax_enemy = 0,screen_size[0]-player_size[0],screen_size[0]-enemy_size[0] #could index 1 and see if they can debug
Ymax_enemy = playerY - enemy_size[1]

#ask user how fast they want to go
speed = float(input('From 1-10, how fast do you want to move?'))
enemy_speed = float(input('From 1-10, how fast do you want enemies to move?'))

def player(x,y):
    """
    blit is like drawing on a game screen. Each frame we want out program to blit the player character on the game screen
    """
    screen.blit(playerImg, (x,y))
    
def enemy(x,y,i):
    screen.blit(space_invador[i], (x,y))
    
def fire_bullet(x,y):
    global bullet_state
    """
    Fired when the bullet gets shot with space bar
    """
    bullet_state = 1
    screen.blit(bullet, ((x + player_size[0]/4), y+player_size[0]/2))
    
def is_collision(x1,y1,x2,y2,enemy_size):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    if d < enemy_size: return True
    else: return False

#%%

#unless we create a quit functionality we can't shut the window
running = True
#make sure the screen stays up
while running:
    
    #lets modify what this background looks like
    #try color to rgb!        
    screen.fill((0,200,0)) #rgb like we did before!
    #add background
    screen.blit(background,(0,0))
    
    #player must be after the screen fill!
    player(playerX,playerY)
    playerX += direc*speed
    
    if bullet_state:        #can't have this in for loop or bullet goes up too fast
            bulletY -= bullet_speed
            fire_bullet(bulletX,bulletY)
        
    for i in range(difficulty):
        enemy(enemyX[i],enemyY[i],i)    #as soon as we put this in check its there
        enemyX[i] += enemy_direc[i] * enemy_speed
        
        if enemyX[i] <= Xmin or enemyX[i] >= Xmax_enemy:
            enemy_direc[i] = -enemy_direc[i]
            enemyY[i] += enemy_size[1]
    
        if bullet_state:        #can't have this in for loop or bullet goes up too fast
            collision = is_collision(bulletX,bulletY,enemyX[i],enemyY[i],32)
            if bulletY < 0: 
                bullet_state = 0
                bulletY = playerY
            elif collision:
                score += 1
                bullet_state = 0
                bulletY = playerY
                enemyX[i], enemyY[i] = random.randint(0,screen_size[0]-enemy_size[0]),50
            
    pygame.display.update() #otherwise the pygame screeen will stay black
    
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
            if event.key == pygame.K_SPACE:
                if not bullet_state:
                    fire_bullet(playerX,bulletY)
                    bulletX = playerX
        #have to stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('direction released')
                direc = 0
    
    if playerX <= Xmin:
        playerX = Xmin
    elif playerX >= Xmax_player:
        playerX = Xmax_player
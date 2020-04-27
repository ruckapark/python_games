# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:38:44 2020

@author: George
"""

import os
import pygame
import random

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
    MOUSEBUTTONDOWN
)

colors = {'red':(255,0,0),
          'green':(0,255,0),
          'blue':(0,0,255),
          'yellow':(255,255,0),
          'black':(0,0,0),
          'white':(255,255,255),
          'cyan':(0,255,255),
          'magenta':(255,0,255),
          'grey':(128,128,128),
          'purple':(128,0,128),
          'maroon':(128,0,0)}

pygame.init()
screen_w,screen_h = 500,500                             #screen size
screen = pygame.display.set_mode((screen_w, screen_h))  #display screen
pygame.display.set_caption("Flappy Python")

#FONTS
font = pygame.font.Font('freesansbold.ttf',32)
smallFont = pygame.font.Font('freesansbold.ttf',20)
tinyFont = pygame.font.Font('freesansbold.ttf',12)

#gravity constants (play around with them!)
python_constant = 2.71*10**(-3)
acc = 9.81 * python_constant

os.chdir('FB_pictures')

#%% CLASSES!!!
class Background():
    def __init__(self):
        #just automatically default to the thunder image
        self.image = pygame.image.load('thunder_bg.jpg')
        self.x = 0       #background start far left and will move right
        self.w = 1920*2  #width we gave in the initilisation stage
        
    def reset(self,theme):
        """
        reset the background image with a desired jpg
        """
        self.image = pygame.image.load('{}_bg.jpg'.format(theme))
    
    def draw(self,screen):
        screen.blit(self.image,(self.x,0))
        
    def move(self):
        self.x -= 1
    
class Python():
    def __init__(self,screen_h):
        self.image = pygame.image.load('flappy_python.PNG')
        self.x = 150
        self.y = screen_h//3
        self.y_diff = 0
        self.old_speed = 0
        self.speed = 0
        
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
        
    def reset(self):
        self.__init__(screen_h)
        
    def suvat(self):
        global acc
        self.speed = self.old_speed + acc
        self.y_diff = 0.5*(self.old_speed + self.speed)
        
    def move(self):
        #bird
        self.old_speed = self.speed
        self.suvat()
        self.y += self.y_diff
        self.draw(screen)
    
class Pipe():
    def __init__(self,screen_w,width = 152,height = 500,speed = 2):
        self.image = pygame.image.load('pipe.PNG')
        self.x = screen_w
        self.y = -random.randint(110,490)
        self.height = height
        self.width = width
        self.gap = 100
        self.speed = speed
        self.passed = False
        
    def draw(self,screen,x,y):
        screen.blit(self.image,(x,y))
    
    def reset(self):
        self.__init__(screen_w)
    
    def move(self):
        global screen_w
        self.x -= self.speed
        self.draw(screen,self.x,self.y)
        self.draw(screen,self.x,self.y + self.height + self.gap)
        
        #check if pipe is out of screen and reset it
        if self.x < 0-self.width:
            self.x = screen_w
            self.y = -random.randint(110,490)
            self.edge = 0
            
            
#%%
def show_score(x,y):
    global score_value
    score = font.render('Score: {}'.format(score_value),True,(255,255,255))
    screen.blit(score,(x,y)) 

#%% object assignment
bg_themes = 'thunder desert'.split() #we can add more later!
bg = Background()
python = Python(screen_h)
pipe1 = Pipe(screen_w)
pipe2 = Pipe(screen_w)

def game():
    running = True
    while running:
        
        #background
        screen.fill((255,255,255))
        bg.draw(screen)
        bg.move()
        show_score(10,10)
            
        #pipes
        pipe1.move()
        #pipe2.move()
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                running = False
                
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    python.speed = -1.8
                
        python.move()
        
        if python.y > screen_h or python.y < -32:
            running = False
            score_value = 0
        
        if python.x - pipe1.width < pipe1.x < python.x:
            pipe1.passed = True
            if python.y < (pipe1.y + pipe1.height) or python.y > (pipe1.y + pipe1.height + pipe1.gap):
                #you lose
                running = False
                score_value = 0
                
        if pipe1.x < python.x - pipe1.width and pipe1.passed:
            score_value += 1
            pipe1.passed = False
                
        pygame.display.update()
    
game()
pygame.quit()
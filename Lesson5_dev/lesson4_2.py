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
    
def game():
    running = True
    while running:
        screen.fill((255,255,255))
        
    for event in pygame.event.get():
        
        if event.type == QUIT:
            running = False
    
    pygame.display.update()
    
game()
pygame.quit()
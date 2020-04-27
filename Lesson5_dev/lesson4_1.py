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
        pass
    
class Python():
    def __init__(self):
        pass
    
class Pipe():
    def __init__(self):
        pass
    
def game():
    running = True
    while running:
        screen.fill((255,255,255))
        
    for event in pygame.event.get():
        
        if event.type == QUIT:
            #quit game loop
            running = False
    
    pygame.display.update()
    
game()
pygame.quit()
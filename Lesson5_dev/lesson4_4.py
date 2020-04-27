# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:04:11 2020

Flappy Python code

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

#%% start variables and global variables
pygame.init()
screen_w,screen_h = 500,500                             #screen size
screen = pygame.display.set_mode((screen_w, screen_h))  #display screen
pygame.display.set_caption("Flappy Python")
score_value = 0
click = False

#FONTS
font = pygame.font.Font('freesansbold.ttf',32)
smallFont = pygame.font.Font('freesansbold.ttf',20)
tinyFont = pygame.font.Font('freesansbold.ttf',12)

#gravity constants (play around with them!)
python_constant = 2.71*10**(-3)
acc = 9.81 * python_constant

#be in  the pictures folder before starting the code!
os.chdir('FB_pictures')

#%% CLASSES!!!

class Background():
    def __init__(self):
        self.image = pygame.image.load('thunder_bg.jpg')
        self.x = 0
        self.w = 1920*2
        
    def reset(self,theme):
        self.image = pygame.image.load('{}_bg.jpg'.format(theme))
        
    def draw(self,screen):
        screen.blit(self.image,(self.x,0))
        
    def move(self):
        self.x -= 1
        if -self.w < self.x <= -self.w + 500:
            screen.blit(self.image,(self.x+self.w,0))
        elif self.x <= -self.w:
            self.x = 0
            screen.blit(self.image,(self.x,0))
        
#player icon is a python
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
            
class Button():
    
    def __init__(self,x,y,w,h):
        self.x = x #topleft button
        self.y = y #topleft
        self.w = w #width
        self.h = h #thickenss
        self.button = pygame.Rect(x,y,w,h)
        
    def text_objects(self,text,font,color):
        self.surf = font.render(text, True, color)
        self.rect = self.surf.get_rect()
        self.rect.center = (self.x + self.w/2,self.y + self.h/2) #center the text in the rectangle

    def draw_button(self,screen,color):
        pygame.draw.rect(screen,color,self.button)
    
    def button_text(self,screen):
        screen.blit(self.surf,self.rect)
        
    def check_mouse(self,mx,my,color_idle,color_collide):
        global click
        if self.button.collidepoint((mx,my)):
            self.draw_button(screen,color_collide)
            if click:
                click = False
                return True
        else:
            self.draw_button(screen,color_idle)
            return False

#%% Stand alone functions!        
def draw_text(text,font,color,surface,x,y):
    """
    function to draw text without requiring a button
    """
    textobj = font.render(text,True,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
    
def show_score(x,y):
    global score_value
    score = font.render('Score: {}'.format(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


#%% onject assignment
bg_themes = 'thunder desert'.split() #we can add more later!
bg = Background()
python = Python(screen_h)
pipe1 = Pipe(screen_w)
pipe2 = Pipe(screen_w)

# BUTTONS
button_easy = Button(100,150,100,30)
button_medium = Button(200,150,100,30)
button_hard = Button(300,150,100,30)
button_thunder = Button(50,400,175,50)
button_desert = Button(275,400,175,50)
button_easy.text_objects('easy',tinyFont,colors['magenta'])
button_medium.text_objects('medium',tinyFont,colors['magenta'])
button_hard.text_objects('hard',tinyFont,colors['magenta'])
button_thunder.text_objects('THUNDER',smallFont,colors['green'])
button_desert.text_objects('DESERT',smallFont,colors['green'])

#%% Two different screens each contained within functions (main menu and the game)
def menu():
    global click
    global acc
    click = False #define at beginning of code as global variable
    running = True
    
    while running:
        
        python.reset()
        pipe1.reset()
        pipe2.reset()
        
        screen.fill((255,255,255))
        bg.draw(screen)
        bg.move()
        draw_text('Main Menu', font, colors['white'], screen, 20,20)
        
        mx,my = pygame.mouse.get_pos()
        
        #check background
        if button_thunder.check_mouse(mx,my,colors['cyan'],colors['blue']):
            bg.reset('thunder')
            game()
        elif button_desert.check_mouse(mx,my,colors['cyan'],colors['blue']):
            bg.reset('desert')
            game()
        
        #check game settings
        if button_easy.check_mouse(mx,my,colors['black'],colors['green']):
            #change game settings to easy
            acc = 9.81*1.5 * python_constant #less gravity is harder ! try it!
        elif button_medium.check_mouse(mx,my,colors['black'],colors['yellow']):
            #change game settings to medium
            acc = 9.81 * python_constant
        elif button_hard.check_mouse(mx,my,colors['black'],colors['red']):
            #change game setting to hard
            acc = 9.81/1.3 * python_constant
        
        button_easy.button_text(screen)
        button_medium.button_text(screen)
        button_hard.button_text(screen)
        button_thunder.button_text(screen)
        button_desert.button_text(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()

def game():
    """
    If we die it reverts back to menu!
    """
    global score_value
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
    
menu()
pygame.quit()
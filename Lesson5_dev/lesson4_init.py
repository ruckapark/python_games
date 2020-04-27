# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 19:44:58 2020

@author: George
"""

import os
import PIL
from PIL import ImageOps #PIL.ImageOps doesnt work for me?

base_dir = os.getcwd()

# create directory called 'FB_pictures'
if 'FB_pictures' not in os.listdir():
    os.mkdir('FB_pictures')
    
os.chdir('FB_pictures')

#load in pipe picture from gaming pictures, and resize it to be 500 pixels high (keep width in proportion)
if 'pillar.PNG' in os.listdir():
    pipe = PIL.Image.open('pillar.PNG')
    pipe_size = pipe.size
    pipe.resize((int(341*(500/1121)),500)).save('pipe.PNG')
else:
    #assume already there
    pass

#load in background, make mirror, merge mirror to the left and use this as the background to avoid messy screen transition
thunder_bg_left = PIL.Image.open(r'C:\Users\George\Pictures\Gaming\thunder.jpg').crop((0,658,1920,1158))
thunder_bg_left.show()

thunder_bg_right = ImageOps.mirror(thunder_bg_left)

thunder_bg = PIL.Image.new('RGB', (1920*2, 500))
thunder_bg.paste(thunder_bg_left,(0,0))
thunder_bg.paste(thunder_bg_right,(1920,0))

thunder_bg.save('thunder_bg.jpg')

#take in one of the space invaders as our flappy python
python = PIL.Image.open(r'C:\Users\George\Documents\TechCamp\CourseDesign\python_games\SI_pictures\space_invader.PNG')
python.save('flappy_python.PNG')
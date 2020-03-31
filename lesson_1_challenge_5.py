# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 16:39:12 2020

@author: George
"""

"""
Let's see if we can get all the photos we were using in the same crop size

We also want to use the python logo in a few different colours.
See if you can go back to the code from the lesson and play with the rgb filters

Once you're happy with three different colour combos from blue, yellow

ie. ?,?,?

Save them to a new folder below
Follow the code below.
"""

# you will need to import os and PIL libraries
#you only need Image from PIL!
import os
from PIL import Image, ImageDraw

#create a directory called Flappy_bird_backgrounds
if 'Flappy_bird_backgrounds' not in os.listdir():
    os.mkdir('Flappy_bird_backgrounds')
    
#go into the Game_pictures directory before reading the pictures
os.chdir('Game_pictures')

#use the following photos for backgrounds
#['city.JPG','countryside.JPG','sea.JPG']
images = {}
files = ['thunder.jpg','city.jpg','countryside.jpg','sea.jpg']

#crop all the pictures to the size: 1920,600
image_width = 1920
image_height = 500

for file in files:
    name = file.split('.')[0]
    images.update({name:Image.open(file)})
    
#%% crops
images['city'].crop((0,0,image_width,image_height)).show()
images['countryside'].crop((0,0,image_width,image_height)).show()
offset = 250
images['sea'].crop((0,offset,image_width,image_height + offset)).show()
offset = 350
images['thunder'].crop((0,offset,image_width,image_height + offset)).show()

#once happy change directory to the background picture library
os.chdir('..')
os.chdir('Flappy_bird_backgrounds')
images['city'].crop((0,0,image_width,image_height)).save('city_background.jpg')
images['countryside'].crop((0,0,image_width,image_height)).save('countryside_background.jpg')
images['sea'].crop((0,250,image_width,image_height + 250)).save('sea_background.jpg')
images['thunder'].crop((0,350,image_width,image_height + 350)).save('thunder_background.jpg')


#%% let's also have a go at making various colour schemes for our characters
os.chdir('..')
os.chdir('Game_pictures')
python = Image.open('python.png')
r,g,b,a = python.split()

Image.merge("RGBA",(b,g,r,a)).show()
Image.merge("RGBA",(g,b,r,a)).show()
Image.merge("RGBA",(b,r,g,a)).show()
python.convert('LA').show()

Image.merge("RGBA",(b,g,r,a)).resize((64,64)).save('enemy1.PNG')
Image.merge("RGBA",(g,b,r,a)).resize((64,64)).save('enemy2.PNG')
Image.merge("RGBA",(b,r,g,a)).resize((64,64)).save('enemy3.PNG')
python.convert('LA').resize((64,64)).save('enemy4.PNG')

os.chdir('..')
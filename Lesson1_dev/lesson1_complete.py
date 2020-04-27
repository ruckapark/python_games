# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:23:03 2020

Reset spyder settings (plotting in automatic)

File and Variable explorer are useful!

We can actually run things in the bottom right just via the console (a bit like jupyter!)

@author: George
"""

#%%
#this part of the code is text

#print hello world
print('Hello World!')

#print names and ages with format and without
names = ['George','Hatty']
ages = [24,21]
print(names[0],' is ',ages[0])
print('{} is {} 20 years old'.format(names[1],ages[1]))

#take the sum of the two ages
print(ages[0] + ages[1])

#%%
#What are some game characters?
chars = ['Mario','Luigi','Princess']

#add one more
chars.append('Toad')

#make a for loop and output the first letter of each name of character
for char in chars:
    print(char,'s first letter is',char[0])
        
#%%
#import numpy, using nothing, as and from. floor and ceiling are two good examples
import numpy
x,y = 10.8,22.4
print(numpy.ceil(x))
print(numpy.floor(y))

import numpy as np
print(np.ceil(x/y))
print(np.floor(y/x))

#numpy array is NOT like a list!
array1 = np.array([1,3,2,5,2])
array2 = np.array([3.1,4,5.4,6.2,4.1])
print(array1 + array2)
print(array1/array2)

from numpy import ceil
print(ceil(array2))




#%% try using random another library
import random
print('three random numbers between 0 and 10')
for i in range(3):
    print(random.randint(0,10))

print('three random numbers between 20 and 25')
for i in range(3):
    print(random.randint(20,25))

print('three random numbers between 0 and 1')
for i in range(3):
    print(random.random())

#%% import os
import os

folder_path = os.getcwd()
print('This is where the computer is working:')
print(folder_path)

#show how to list the files, get the root of the files, make a new folder
files = os.listdir()
print('These are the files in the current folder:')
print(files)

#save the base directory and go forward one, then go back one.
os.chdir('Pictures')
pics_directory = os.getcwd()
print('Now we are in this directory:',pics_directory)
os.chdir('..')
print('Double .. gets rid of the last "/" so we go back to:',os.getcwd())

#go back two more and see where we are
os.chdir('..')
os.chdir('..')
print(os.getcwd())

#go all the way back into the pictures directory
os.chdir(pics_directory)
print(os.getcwd())

#go back to the old one
os.chdir('..')

#%% import PIL and a class called ImageOps
import PIL
from PIL import ImageOps

#list the direcctory in the console and then change to the picture file in your computer.
os.chdir('Pictures')

#save this directory as the pics_dir
pics_dir = os.getcwd()

#open image with PIL saved to an object and have a look in explorer window
image = PIL.Image.open('thunder.jpg')
image.show()

#show it. then play with resize and crop
pixels_x = 10
pixels_y = 10
image.resize((pixels_x,pixels_y)).show()
image.crop((0,0,pixels_x,pixels_y)).show()

pixels_x = 100
image.resize((pixels_x,pixels_y)).show()
image.crop((0,0,pixels_x,pixels_y)).show()

pixels_y = 500
image.resize((pixels_x,pixels_y)).show()
image.crop((0,0,pixels_x,pixels_y)).show()

#%% save the dimensions using size()
image_width = image.size[0]
image_height = image.size[1]

#flappy bird doesn;t need a tall picture but we want a long one in x
new_height = 200
image.crop((0,500,image_width,500 + new_height)).show()

#play around with using crop until we are happy with a 500 tall picture with x staying the same
new_height = 500
image.crop((0,500,image_width,500 + new_height)).show()
image.crop((0,650,image_width,650 + new_height)).show()

thunder_image = image.crop((0,650,image_width,650 + new_height)).show()

#then make a new directory in the console called 'FB_pictures' - check in correct directory
os.chdir('..')
if 'FB_pictures' not in os.listdir():
    os.mkdir('FB_pictures')
os.chdir('FB_pictures')
FB_dir = os.getcwd()

#save the pictures in a list and open them in turn using a for loop!
pictures = ['countryside.jpg','city.jpg','sea.jpg']
images = [thunder_image]
for picture in pictures:
    images.append(PIL.Image.open(picture))

#%% now lets try opening the python image - PNG!
python = PIL.Image.open('python.PNG')

#check the image mode in the console. A allows a transparent layer.
print('This photo type is:',python.mode)

#make it greyscale using 'LA'
python.convert('LA').show()

# r,g,b,a split()
r,g,b,a = python.split()

# merge PIL.Image.merge('RGBA',)
PIL.Image.merge('RGBA',(g,r,b,a)).show()
PIL.Image.merge('RGBA',(g,g,b,a)).show()
PIL.Image.merge('RGBA',(g,b,r,a)).show()

new_python1 = PIL.Image.merge('RGBA',(g,r,b,a))
new_python1.resize((64,64)).save('python_purple.PNG')



















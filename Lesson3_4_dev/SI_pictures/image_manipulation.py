# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:12:53 2020

@author: George
"""

import PIL
import os

#raw string allows us to have slashed in without confusion to get to my path (unique)
os.chdir(r'C:\Users\George\Documents\TechCamp\CourseDesign\python_games\SI_pictures')

#check for exact file names
files = os.listdir()

#open space invader
image = PIL.Image.open('space_invader.PNG')
image.show()

#check it is RGBA and not RGB (A is alpha for transparence)
type_image = image.mode

#split into three images, one with all the red, one the green etc.
r,g,b,a = image.split()

#play around with the order of rgb and we'll get new colours!!!
PIL.Image.merge(type_image,(r,b,g,a)).save('space_invader2.PNG')
PIL.Image.merge(type_image,(g,r,b,a)).save('space_invader3.PNG')
PIL.Image.merge(type_image,(b,r,g,a)).save('space_invader4.PNG')
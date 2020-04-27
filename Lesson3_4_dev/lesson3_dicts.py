# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:42:30 2020

@author: George
"""

"""
Dictionaries are like a lookup book - phonebook, dictionary etc.
"""
#%%
dictionary = {
        'hello':'A greeting used in the english language when meeting someone',
        'goodbye':'A farewell in the englihs language'
        }

phonebook = {
        'Max':1334258394,
        'Dad':1367422152
        }

phonebook.update({
        'Mum':7957121425
        })

print(dictionary)
print(dictionary['hello'])

mario = {
        'name':'Mario',
        'height':65,
        'speed':5,
        'colour':'red'
        }

for key in mario:
    print(key,'=',mario[key])
    
"""
Exercises: Make a dictionary of colours, in the keys add the colour name 
           with the (r,g,b) value after the key.
           Example below (add more colors!):
"""

colors = {'red':(255,0,0),'green':(0,255,0),'blue':(0,0,255)}
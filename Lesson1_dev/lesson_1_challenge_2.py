# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:32:48 2020

An example of a simple twenty questions style game

@author: George
"""

cats = ['cat','lynx','tiger','lion','puma','panther','leopard','jaguar','cheetah']

print("Think of any type of feline (cat), I'll ask you some questions and guess which one you're thinking of!")
question1 = input('How big is the cat? - small, medium,large?')
if question1 == 'small':
    question2 = input('Is it a pet? - y/n')
    if question2 =='y':
        print('Its a cat!')
    else:
        print('Its a lynx')
elif question1 == 'medium':
    question2 = input('Is it the fastest land animal? - y/n')
    if question2 == 'Y':
        print('Its a cheetah!')
    else:
        question3 = input('Does it live in Africa? - y/n')
        if question3 == 'y':
            print('Its a leopard!')
        else:
            print('Its a jaguar!')
else:
    question2 = input('Do males have manes? - y/n')
    if question2 == 'y':
        print('Its a lion!')
    else:
        print('Its a tiger!')
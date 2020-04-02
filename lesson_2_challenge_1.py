# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:28:02 2020

Two of the most important things in python - functions and classes

Follow the instructions below to complete the following challenge !

@author: George
"""
def max_of_three(a,b,c):
    """
    Write a Python function to find the Max of three numbers
    
    in reality we would just use the python inbuilt function!
    """
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b 
    else:
        return c
    
def rev_str(string):
    """
    Write a Python program to reverse a string
    
    This is the quickest way but there are lots of others!
    """
    print(string[::-1])
    return string[::-1]

def unique_counts(list_):
    """
    Write a Python function that takes a list and returns a new list with unique elements of the first lis
    """
    new_list = []
    for element in list_:
        if element not in new_list: new_list.append(element)
        
def if_palindrome(string):
    """
    Write a Python function that checks whether a passed string is palindrome or not. 
    """
    if string == string[::-1]: 
        return True
    else: 
        return False

def move(direction, coordinates):
    """
    Possible directions passed are 'L','R','U','D'
    
    Assuming a normal coordinate system return the new coordiates (x,y) after moving
    """
    x,y = coordinates[0],coordinates[1]
    #if elif elif else for the four directions
    if direction == 'L':
        x -= 1
    elif direction == 'R':
        x += 1
    elif direction == 'U':
        y += 1
    elif direction == 'D':
        y -= 1
    return [x,y]
    
# now try to get you're player from (0,3) to (13,3) in one line of code


def fibonacci_recursive(n):
    """
    See if you can make a fibonacci sequence using a recursive function
    """
    print("Calculating F({})".format(n),end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
class enemy():
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed
        
    def move(self,direction):
        if direction == 'L':
            self.position[0] -= self.speed
        elif direction == 'R':
            self.position[0] += self.speed
            
        print(self.position)

import random
class enemy_update():
    def __init__(self):
        self.position = [random.randint(1,10),15]
        self.speed = random.randint(1,5)
        
    def move(self,direction):
        if direction == 'L':
            self.position[0] -= self.speed
        elif direction == 'R':
            self.position[0] += self.speed
        elif direction == 'U':
            self.position[1] += self.speed/2
        elif direction == 'D':
            self.position[1] -= self.speed/2
            
        print('enemy is moving {} \nit is now located at {}'.format(direction,self.position))
        
enemy1 = enemy([10,15],3)
enemy1.move('L')

enemy2 = enemy_update()
enemy2.move('D')